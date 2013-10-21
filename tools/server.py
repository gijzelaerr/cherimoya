"""
Basic server which spits out random protocol 0 data, used for testing
"""
import socket
import time
import logging
from thread import *


logger = logging.getLogger(__name__)

host = ''
port = 6667
protocol_ver = 0


def conn_handler(conn):
    while True:
        conn.sendall('hello!')
        time.sleep(1)
    conn.close()


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        logger.info('%s:%s connected' % (addr[0], addr[1]))

    start_new_thread(conn_handler, (conn,))


if __name__ == '__main__':
    server()