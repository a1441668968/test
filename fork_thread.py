# import os
#
# pid = os.fork()
# if pid:
#     print(pidy)
# else:
#     print('c')
# print('end')
###################################################################
# import subprocess
# import os
#
#
# def ping(host):
#     result = subprocess.call(
#         'ping -c2 %s &> /dev/null' % host, shell=True
#     )
#     if result == 0:
#         print('%s is up' % host)
#     else:
#         print('%s is down' % host)
#
#
# if __name__ == '__main__':
#     ip_pool = ['192.168.4.%s' % i for i in range(1, 255)]
#     for ip in ip_pool:
#         pid = os.fork()
#         if not pid:
#             ping(ip)
#             exit()
#############################################################################
# import os
# import time
#
#
# def fork(pt, ct):
#     pid = os.fork()
#     if pid:
#         time.sleep(pt)
#         print(os.waitpid(-1, 1))
#     else:
#         time.sleep(ct)
#
# fork(3, 5)
# fork(10, 5)
############################################################
# import subprocess
# import threading
#
#
# def ping(host):
#     result = subprocess.call(
#         'ping -c2 %s &> /dev/null' % host, shell=True
#     )
#     if result == 0:
#         print('%s is up' % host)
#     else:
#         print('%s is down' % host)
#
#
# if __name__ == '__main__':
#     ip_pool = ['192.168.4.%s' % i for i in range(1, 255)]
#     for ip in ip_pool:
#         t = threading.Thread(target=ping, args=(ip,))
#         t.start()
############################################################
# import threading
# import subprocess
#
#
# class Ping:
#     def __init__(self,host):
#         self.host = host
#
#     def __call__(self):
#         result = subprocess.call(
#             'ping -c2 %s &> /dev/null' % self.host, shell=True
#         )
#         if result == 0:
#             print('%s is up' % self.host)
#         else:
#             print('%s is down' % self.host)
#
#
# if __name__ == '__main__':
#     ip_pool = ['192.168.4.%s' % i for i in range(1, 255)]
#     for ip in ip_pool:
#         t = threading.Thread(target=Ping(ip))
#         t.start()
################################################################
import time
import os
import threading


def calc():
    result = 0
    for i in range(50000000):
        result += i
    print(result)


if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        calc()
    end = time.time()
    print(end - start)
    start = time.time()
    for i in range(2):
        pid = os.fork()
        if not pid:
            calc()
            exit()
    os.waitpid(-1, 0)
    end = time.time()
    print(end - start)
    start = time.time()
    for i in range(2):
        t = threading.Thread(target=calc)
        t.start()
    t.join()
    end = time.time()
    print(end - start)
