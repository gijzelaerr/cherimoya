import socket
from datetime import datetime
import logging
from cherimoya.common import jul_unix_diff
from cherimoya import settings

logger = logging.getLogger(__file__)


max_timestamp = 1342058400
then = datetime.fromtimestamp(max_timestamp)
now = datetime.now()
compensate = (now - then).total_seconds()


def readline(sock):
    """reads newline terminated lines from a socket. Yields lines.

    :param sock: a python socket
    :return: yields stripped lines
    """
    buffer_ = sock.recv(4096)
    done = False
    while not done:
        if "\n" in buffer_:
            (line, buffer_) = buffer_.split("\n", 1)
            yield line
        else:
            more = sock.recv(4096)
            if not more:
                done = True
            else:
                buffer_ = buffer_ + more
    if buffer_:
        yield buffer_


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
    assert ver == "0"
    timestamp = datetime.fromtimestamp(float(timestamp) - jul_unix_diff + compensate)
    values = []
    for index, field in enumerate(fields.split()):
        value = parse(field)
        values.append((index, value))
    return timestamp, label, values


def lineformat(label, index, value, timestamp, multiple=True):
    if multiple:
        postfix = ".%s" % index
    else:
        postfix = ""

    if type(value) == complex:
        metricreal = "%s%s.real" % (label, postfix)
        line = "%s %s %s\n" % (metricreal, value.real, timestamp.strftime("%s"))
        metricimag = "%s%s.imag" % (label, postfix)
        line += "%s %s %s\n" % (metricimag, value.real, timestamp.strftime("%s"))
    else:
        metric = "%s%s" % (label, postfix)
        line = "%s %s %s\n" % (metric, value, timestamp.strftime("%s"))
    return line


def replace_dots(string):
    """
    replace dots with comma's and underscores with dots.

    dots are used by graphite to determine the tree structure, so they can't be
    used.
    """
    return string.replace(".", "-").replace("_", ".")


def client_mainloop():
    """Cherimoya main loop.
    Connects to server and parses results returned.
    """
    aartfaac = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    graphite = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        aartfaac.connect((settings.AARTFAAC_HOST, settings.AARTFAAC_PORT))
        graphite.connect((settings.GRAPHITE_HOST, settings.GRAPHITE_PORT))
        for line in readline(aartfaac):
            timestamp, label, values = parseline(line)
            multiple = bool(max(0, len(values) - 1))
            for index, value in values:
                label_clean = replace_dots(label)
                line = lineformat(label_clean, index, value, timestamp, multiple)
                logging.debug(line.strip())
                graphite.sendall(line)
    finally:
        aartfaac.close()
        graphite.close()

if __name__ == '__main__':
    level = logging.INFO
    if settings.DEBUG:
        level = logging.DEBUG
    logging.basicConfig(level=level)
    client_mainloop()
