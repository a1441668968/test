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
###################################################
# import getpass
# username=input('输入用户名')
# password=getpass.getpass('密码')
# if username=='tom' and password=='123456':
#     print('success')
# else:
#     print('wrong')
#################################################
# import random
# num=random.randint(1,100)
# cai=int(input('你猜的数字'))
# if cai > num:
#     print('猜大了')
# elif cai < num:
#     print('猜小了')
# else:
#     print('恭喜')
# print('正确的是',num)
##################################################
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
##################################################
# import random
# choice=['石头','剪刀','布']
# prompt = '''0.石头
# 1.剪刀
# 2.布
# 请选择(0/1/2):'''
# computer=random.randint(0,2)
# player=int(input(prompt))
# if player not in [0,1,2]:
#     print('瞎选，默认是布')
#     player=2
# print('你选择的是 %s, 计算机选择的是 %s' %(choice[player],choice[computer]))
# c=player-computer
# if c==-1 or c==2:
#     print('\033[31;1m你赢了\033[0m')
# elif c==0:
#     print('\033[32;1m平局\033[0m')
# else:
#     print('\033[31;1m你输了\033[0m')
#################################################
# sum100 = 0
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2 :
#         continue
#     sum100 += counter
# print ("result is %d" % sum100)
# import random
# computer=random.randint(1,10)
# counte=0
# while counte<5:
#     cai=int(input('请输入你猜的数字'))
#     if computer > cai:
#         print('猜小了')
#     elif computer < cai:
#         print('猜大了')
#     else:
#         print('猜对了')
#         break
#     counte+=1
# else:
#     print('正确的是',computer)
###########################################################3
import random
choice=['石头','剪刀','布']
prompt = '''0.石头
1.剪刀
2.布
请选择(0/1/2):'''
computer_win=2
player_win=2
while computer_win and player_win:
    computer=random.randint(0,2)
    player=int(input(prompt))
    if player not in [0,1,2]:
        print('瞎选，默认是布')
        player=2
    print('你选择的是 %s, 计算机选择的是 %s' %(choice[player],choice[computer]))
    c=player-computer
    if c==-1 or c==2:
        print('\033[31;1m你赢了1局\033[0m')
        player_win -= 1
    elif c==0:
        print('\033[32;1m平局\033[0m')
    else:
        print('\033[31;1m你输了1局\033[0m')
        computer_win -= 1
else:
    print('游戏结束')
    if computer_win == 0:
        print('你输了')
    else:
        print('你赢了')