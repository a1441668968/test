#!/usr/local/bin/python3
# f=open('/tmp/passwd')
# data=f.read()
# print(data)
# data=f.read()
# print(data)
# f.close()
# f=open('/tmp/passwd')
# data=f.read(4)
# print(data)
# data=f.readline()
# print(data)
# data=f.readlines()
# print(data)
# f.close()
# f=open('/tmp/passwd')
# for line in f :
#     print(line,end='')
# f.close()
# f=open('/root/1.jpg','rb')
# print(f.read(4096))
# f.close()
# f=open('/tmp/test','w')
# f.write('hello')
# f.flush()
# f.writelines(['world\n','new'])
# f.close()
# with open('/tmp/passwd') as f:
#     print(f.readline(),end='')
# #print(f.readlines())
# f=open('/tmp/passwd')
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# f.seek(0,2)
# print(f.tell())
# f.seek(0,0)
# print(f.tell())
######################################################
# def mk_fib(length=8):
#     "说明文件：这是一个兔子数列"
#     fib=[0,1]
#     for i in range(length-len(fib)):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# print('兔子数列示例：')
# exam=mk_fib()
# print(exam)
# print('-'*50)
# n=int(input('想生成的数列长度：'))
# print(mk_fib(n))
################################################
# import sys
# def copy(src_name,dst_name):
#     src_f=open(src_name,'rb')
#     dst_f=open(dst_name,'wb')
#     while True:
#         data=src_f.read(4096)
#         if not data:
#             break
#         dst_f.write(data)
#     src_f.close()
#     dst_f.close()
# copy(sys.argv[1],sys.argv[2])
#################################################
