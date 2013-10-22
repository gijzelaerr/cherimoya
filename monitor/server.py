"""
Basic server which spits out random protocol 0 data, used for testing
"""
import time
import logging
import socket
import SocketServer
from random import random

prot_ver = 0


logger = logging.getLogger(__file__)

char = lambda x: chr(int(x))

field_types = {
    'EXAMPLE1': (
        (int, (10, 100)),
        (int, (10, 100)),
    ),
    'EXAMPLE2': (
        (float, (0, 1)),
    ),
    'EXAMPLE3': (
        (float, (0, 1)),
        (char, (65, 90)),
    )
}


def generate(props):
    vals = []
    for type_, (start, stop) in props:
        value = start + random()*(stop-start)
        vals.append(str(type_(value)))
    return " ".join(vals)


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


