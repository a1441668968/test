#!/usr/local/bin/python3
import socket

host = ''
port = 12345
addr = (host, port)
client = socket.socket()
client.connect(addr)
while True:
    data = input('> ') + '\n'
    client.send(data.encode('utf8'))
    if data.strip() == 'end':
        break
    data = client.recv(1024)
    print(data.decode('utf8'))
client.close()
