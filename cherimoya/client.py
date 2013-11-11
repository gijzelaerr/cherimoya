import socket
from datetime import datetime
import logging
from cherimoya.db import Statistic, FloatValue, IntValue, Line, StrValue, db
from cherimoya import app

logger = logging.getLogger(__file__)


db.init_app(app)

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


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def detect_type(field):
    if field.isdigit():
        return int
    elif isfloat(field):
        return float
    else:
        return str


def parseline(line):
    ver, timestamp, label, fields = line.split(" ", 3)
    assert ver, 0
    timestamp = datetime.fromtimestamp(float(timestamp))
    values = []
    for index, field in enumerate(fields.split(" ")):
        type_ = detect_type(field)
        values.append((type_, index, type_(field)))
    return timestamp, label, values

type_map = {
    int: IntValue,
    float: FloatValue,
    str: StrValue,
}


def store(timestamp, label, values):
    """Stores a parsed aartfac log line to database.

    :param timestamp: a python timestamp
    :param label: the name of the statistic
    :param values: a list of (type, index, value) tuples
    """
    statistic = Statistic(name=label)
    line = Line(statistic=statistic, moment=timestamp)

    db.session.add_all([statistic, line])
    for type_, index, value in values:
        model = type_map[type_]
        m = model(line=line, index=index, value=value)
        logger.debug("storing %s" % m)
        db.session.add(m)
    db.session.commit()


def client_mainloop(host, port):
    """Cherimoya main loop.
    Connects to server and parses results returned.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        for line in readline(sock):
            timestamp, label, values = parseline(line)
            store(timestamp, label, values)
    finally:
        sock.close()



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    host = app.config['AARTFAAC_HOSTS'][0]['HOST']
    port = app.config['AARTFAAC_HOSTS'][0]['PORT']
    client_mainloop(host, port)