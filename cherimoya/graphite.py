import socket
from datetime import datetime
import logging

logger = logging.getLogger(__file__)

seconds_between_julian_and_unix_epoc = 3506716800


AARTFAAC_HOST = 'localhost'
AARTFAAC_PORT = 9999

GRAPHITE_HOST = 'localhost'
GRAPHITE_PORT = 2003


def readline(sock):
    """reads newline terminated lines from a socket. Yields lines.

    :param sock: a python socket
    :return: yields stripped lines
    """
    buffer = sock.recv(4096)
    done = False
    while not done:
        if "\n" in buffer:
            (line, buffer) = buffer.split("\n", 1)
            yield line
        else:
            more = sock.recv(4096)
            if not more:
                done = True
            else:
                buffer = buffer+more
    if buffer:
        yield buffer


def tocomplex(string):
    try:
        r, i = string[1:-1].split(',')
        return complex(float(r), float(i))
    except ValueError:
        raise ValueError("could not convert string to complex: %s" % string)


def parse(string):
    for func in tocomplex, float, int, str:
        try:
            return func(string)
        except ValueError:
            pass


def parseline(line):
    ver, label, timestamp, fields = line.split(" ", 3)
    assert ver, 0
    timestamp = datetime.fromtimestamp(float(timestamp))
    values = []
    for index, field in enumerate(fields.split(" ")):
        value = parse(field)
        values.append((index, value))
    return timestamp, label, values


def lineformat(label, index, value, timestamp):
    if type(value) == complex:
        metricreal = "%s.%s.real" % (label, index)
        line = "%s %s %s\n" % (metricreal, value.real, timestamp.strftime("%s"))
        metricimage = "%s.%s.image" % (label, index)
        line += "%s %s %s\n" % (metricimage, value.real, timestamp.strftime("%s"))
    else:
        metric = "%s.%s" % (label, index)
        line = "%s %s %s\n" % (metric, value, timestamp.strftime("%s"))
    return line


def client_mainloop():
    """Cherimoya main loop.
    Connects to server and parses results returned.
    """
    aartfaac = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    graphite = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        aartfaac.connect((AARTFAAC_HOST, AARTFAAC_PORT))
        graphite.connect((GRAPHITE_HOST, GRAPHITE_PORT))
        for line in readline(aartfaac):
            timestamp, label, values = parseline(line)
            for index, value in values:
                line = lineformat(label, index, value, timestamp)
                print(line.strip())
                graphite.sendall(line)
    finally:
        aartfaac.close()
        graphite.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    client_mainloop()
