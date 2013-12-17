"""
Basic server which spits out random protocol 0 data, used for testing
"""
import time
import logging
import socket
import SocketServer
from cherimoya import settings
from cherimoya.common import jul_unix_diff

prot_ver = 0
logger = logging.getLogger(__file__)


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
            for field, props in settings.FIELD_TYPES.items():
                timestamp = time.time() + jul_unix_diff
                data = "%s %s %s %s" % (prot_ver, field, timestamp,
                                        generate(props))
                logger.debug("sending {}".format(data))
                if not self.send(data):
                    logging.warning("connection closed!")
                    return
            time.sleep(1)
            logging.debug("sleeping a second")


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def server_mainloop(host, port):
    logger.info("running server at %s:%s" % (host, port))
    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.serve_forever()


if __name__ == '__main__':
    level = logging.INFO
    if settings.DEBUG:
        level = logging.DEBUG
    logging.basicConfig(level=level)
    server_mainloop(settings.AARTFAAC_HOST, settings.AARTFAAC_PORT)