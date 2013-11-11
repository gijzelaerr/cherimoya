"""
Basic server which spits out random protocol 0 data, used for testing
"""
import time
import logging
import socket
import SocketServer
import random
from cherimoya import app

prot_ver = 0


logger = logging.getLogger(__file__)


def float_generator(start, end):
    """
    returns a function that generates random float in the range start - end.
    """
    return lambda: start + random.random()*(end-start)


def int_generator(start, end):
    """
    returns a function that generates random ints in the range start - end.
    """
    return lambda: int(start + random.random()*(end-start))


def str_generator(choices):
    """
    returns a function that generates random choices from `choices`.
    """
    return lambda: random.choice(choices)



field_types = {
    'EXAMPLE1': (
        float_generator(10, 100),
        float_generator(0, 5),
    ),
    'EXAMPLE2':
        50 * [int_generator(0, 100)],
    'EXAMPLE3': (
        str_generator(["LBA0", "LBA1", "HBA_SPLIT"]),
    ),
}


def generate(props):
    return " ".join([str(f()) for f in props])


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def send(self, data):
        try:
            self.request.sendall('%s\n' % data)
            return True
        except socket.error:
            return False

    def handle(self):
        logger.info("%s:%s connected" % self.client_address)
        while True:
            for field, props in field_types.items():
                timestamp = time.time()
                data = "%s %s %s %s" % (prot_ver, timestamp,
                                        field, generate(props))
                logger.debug("sending {}".format(data))
                if not self.send(data):
                    break
            time.sleep(1)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def server_mainloop(host, port):
    logger.info("running server at %s:%s" % (host, port))
    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    host = app.config['AARTFAAC_HOSTS'][0]['HOST']
    port = app.config['AARTFAAC_HOSTS'][0]['PORT']
    server_mainloop(host, port)