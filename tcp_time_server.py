import socket
import time
import os


class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.addr)
        self.server.listen(1)

    def chat(self, client_sock):
        while True:
            data = client_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (time.strftime('%H:%M:%S'), data.decode('utf8'))
            client_sock.send(data.encode('utf8'))

    def mainloop(self):
        while True:
            try:
                client_sock,client_addr=self.server.accept()
            except KeyboardInterrupt:
                break
            pid=os.fork()
            if pid:
                while True:
                    result=os.waitpid(-1,1)
                    if result[0]==0:
                        break
                client_sock.close()
            else:
                self.server.close()
                self.chat(client_sock)
                exit()
        self.server.close()


if __name__ == '__main__':
    s = TcpTimeServer
    s.mainloop()
