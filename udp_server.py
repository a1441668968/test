#!/usr/local/bin/python3
import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(addr)
while True:
    data, client_addr = server.recvfrom(1024)
    clock = strftime('%H:%M:%S')
    data = data.decode('utf8')
    data = '[%s] %s' % (clock, data)
    server.sendto(data.encode('utf8'))
server.close()