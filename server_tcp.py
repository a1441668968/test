#!/usr/local/bin/python3
import socket

host = ''
port = 12345
address = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(address)
s.listen(1)
while True:
    cli_sock, cli_address = s.accept()
    print(cli_address)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'end':
            break
        print(data.decode('utf8'))
        data = input() + '\n'
        cli_sock.send(data.encode('utf8'))
    cli_sock.close()
s.close()
