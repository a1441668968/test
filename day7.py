#!/usr/local/bin/python3
# import re
# m=re.match('f..','food')
# print(m.group())
# m=re.search('foo','seafood')
# m=re.findall('foo','seafood is food')
# for m in re.finditer('f..','seafood is food'):
#     print(m.group())
# m=re.sub('f..','123','fish is food')
# m=re.split('\.','192.168.1.1')
# patt=re.compile('f..')
# m=patt.search('seafood')
###########################################################
# import re
# from collections import Counter
#
#
# class Count_Patt:
#     def __init__(self, fname):
#         self.fname = fname
#
#     def count_patt(self, patt):
#         cpatt = re.compile(patt)
#         result = Counter()
#         with open(self.fname) as f:
#             for line in f:
#                 m = cpatt.search(line)
#                 if m:
#                     result.update([m.group()])
#         return result
#
#
# if __name__ == '__main__':
#     cout = Count_Patt('access_log')
#     ip = '^(\d+\.){3}\d+'
#     br = 'Firefox|MSIE|Chrome'
#     result = cout.count_patt(ip)
#     print(result.most_common())
#     print(cout.count_patt(br))
###############################################################
import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()
client_sock, client_addr = s.accept()
print(client_addr)
while True:
    data=client_sock.recv(1024)
    if data.strip()==b'end':
        break
    print(data.decode('utf8'))
    data=input('> ')+'\n'
    client_sock.send(data.encode('utf8'))
client_sock.close()
s.close()
