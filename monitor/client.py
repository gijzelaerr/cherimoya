import socket

host = 'localhost'
port = 9999

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
    parsed = []
    for index, field in enumerate(fields.split(" ")):
        type_ = detect_type(field)
        parsed.append((type_, index, type_(field)))


def client_mainloop(host, port):
    """Cherimoya main loop.
    Connects to server and parses results returned.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        for line in readline(sock):
            print line
    finally:
        sock.close()
