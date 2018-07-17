#!/usr/local/bin/python3
# print('hello world')
# print('hello','world')
# print('hello'+'world')
# print('hello','world',sep='+++')
# print('hello world'*5)
# print('hello world',end='')
# user=input("请输入用户名")
# print("hello",user)
# a=5+6
# print(a)
# a=a+1
# print(a)
# print(False and'5')
# print('1' and'5')
# print(False or '5')
# print('1' or '5')
# print(not False)
# print(not 5)
# a='''hello
# world
# tom'''
# print(a)
# py_str='python'
# py_str[0]
# py_str[2:5]
# py_str[1:]
# py_str[:6]
# py_str[:]
# py_str[::2]
# py_str[1::-1]
# alist=[10,'a','Bob',[1,2,3]]
# len(alist)
# alist[-1]
# alist[2][1]
# alist[-1][1:]
# 'b' in alist[2]
# alist.append(10)
# alist.remove(10)
# user_dict={'name':'bob', 'age':23}
# 'bob' in user_dict
# 'name' in user_dict
# user_dict['name']
# user_dict['sex']='male'
# atuple=(1,2,"tom","alice")
# 'tom' in atuple
# atuple[0]
# if 3>2:
#     print('yes')
# print('done')
# if 10 in [10,20,30]:
#     print('ok')
# if -0:
#     print('haha')
# if [1,'a']:
#     print('hehe')
# if ' ':
#     print('xixi')
# if '':
#     print('lala')
# import getpass
# username=input('输入用户名')
# password=getpass.getpass('密码')
# if username=='tom' and password=='123456':
#     print('success')
# else:
#     print('wrong')
import random
num=random.randint(1,100)
# cai=int(input('你猜的数字'))
# if cai > num:
#     print('猜大了')
# elif cai < num:
#     print('猜小了')
# else:
#     print('恭喜')
# print('正确的是',num)
# num=int(input('成绩'))
# print('成绩是',num)
# if num > 100:
#     print('请勿作弊')
# elif num > 90:
#     print('优秀')
# elif num > 80:
#     print('好')
# elif num > 70:
#     print('良')
# elif num > 60:
#     print('及格')
# elif num < 0:
#     print('你考了一个假试')
# else:
#     print('你要努力')
# a=30
# b=20
# s=a if a<b else b
# print(s)
import random
choice=['石头','剪刀','布']
computer=random.choice(choice)
player=input('请出拳')
print('你选择的是 %s, 计算机选择的是 %s' %(player,computer))
def caiquan(i):
    if i=='石头':
        j=0
    elif i=='剪刀':
        j=1
    elif i=='布':
        j=2
    else:
        print('瞎几把输')
        j=100
    return j
a=caiquan(computer)
b=caiquan(player)
c=b-a
if c==-1 or c==2:
    print('你赢了')
elif c==0:
    print('平局')
elif c>10:
    print('你特么是找死')
else:
    print('你输了')