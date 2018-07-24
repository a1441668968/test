#!/usr/local/bin/python3
import socket

host = ''
port = 12345
addr = (host, port)
client = socket.socket(type=socket.SOCK_DGRAM)
while True:
    data = input('> ')
    if data.strip() == 'end':
        break
    client.sendto(data.encode('utf8'))
    print(client.recvfrom(1024)[0]).decode('utf8')
client.close()
