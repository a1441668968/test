#!/usr/local/bin/python3
# import shutil
#
# with open('/etc/passwd', 'rb') as fsrc:
#     with open('/tmp/user.txt', 'wb') as fdst:
#         shutil.copyfileobj(fsrc, fdst)
#
# shutil.copyfile('/etc/passwd', '/tmp/user2.txt')
# shutil.copy('/etc/passwd', '/tmp')
# shutil.copy2('/etc/passwd', '/tmp')
# shutil.move('/tmp/user.txt', '/var/tmp')
# shutil.copytree('/var/log', '/tmp/log')
# shutil.move('/tmp/log','/var/tmp')
# shutil.rmtree('/var/tmp/log')
# shutil.copymode('/etc/shadow', '/tmp/user2.txt')
# shutil.copystat('/etc/shadow', '/tmp/user2.txt')
# shutil.chown('/tmp/user2.txt', user='mysql', group='mysql')
# shutil.chown('/tmp/user2.txt', group='ceph')
# shutil.chown('/tmp/user2.txt', user='root')
#############################################################
# import keyword
# keyword.kwlist
# keyword.iskeyword('pass')
##############################################################
# import os
#
#
# def get_fname():
#     while True:
#         fname = input('请输入文件名：')
#         if not os.path.exists(fname):
#             break
#         print('%s已存在，请重新输入' % fname)
#     return fname
#
#
# def get_content():
#     content = []
#     print('请输入数据，以end结束')
#     while True:
#         line = input('>')
#         if line == 'end':
#             break
#         content.append(line)
#     print(content)
#     return content
#
#
# def wfile(fname, content):
#     with open(fname, 'w') as f:
#         f.writelines(content)
#
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = ('%s\n' % line for line in content)
#     wfile(fname, content)
#######################################################
# import random
#
# alist = [10, 'jack']
# for ind in range(len(alist)):
#     print('%s %s' % (ind, alist[ind]))
# for ind, val in enumerate(alist):
#     print('%s %s' % (ind, val))
# atuple = [random.randint(1, 100) for i in range(10)]
# sorted(atuple)
# sorted('hello')
# list(reversed(atuple))
##########################################################
# import sys
# import keyword
# import string
#
# first_word = string.ascii_letters + '_'
# all_word = first_word + string.digits
#
#
# def check_id(name):
#     if keyword.iskeyword(name):
#         return '%s是关键字' % name
#     if name[0] not in first_word:
#         return '首字符不符合规则'
#     for index, word in enumerate(name):
#         if word not in all_word:
#             return '第%s个字符不符合规则' % (index + 1)
#     return '%s符合规则' % name
#
#
# if __name__ == '__main__':
#     print(check_id(sys.argv[1]))
##########################################################
# '%s %d %s' % ('bob', -25, 60)
# '%s %d %f' % ('bob', -25, -60.2)
# '%s %d %5.1f' % ('bob', -25, -60.22)
# '%s %d %5.4f' % ('bob', -25, -60.22)
# '%c' % 97
# '%#o' % 11
# '%#x' % 11
# '%10s%5s' % ('name', 20)
# '%-10s%5s' % ('name', 20)
# '%-10s%05d' % ('name', 20)
# '{} is {}'.format('bob', 15)
# '{1} is {0}'.format(15, 'bob')
# '{:<10} is {:<8}'.format('bob', 15)
# '{:<10} is {:>8}'.format('bob', 15)
# '{:<10} is {:0>8}'.format('bob', 15)
# 'my name is {name},age is{age}'.format(name='bob',age=23)
# '姓名：{name},年龄：{age}'.format(**{'name': 'bob', 'age': 23})
# '姓名：{0[0]},年龄：{0[1]}'.format(['bob',23])
###############################################################
# import subprocess
# import sys
# import randpass
#
#
# def add_user(username, password, fname):
#     data = '''用户信息:%s,%s'''
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call('echo %s | passwd --stdin %s' % (password, username), shell=True)
#     with open(fname, 'a')as f:
#         f.write(data % (username, password))
#
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass.gen_pass()
#     add_user(username, password, '/tmp/adduser.txt')
########################################################################
# astr = 'hello world 2018!'
# astr.capitalize()
# astr.title()
# astr.center(50)
# astr.center(50, '-')
# astr.count('w')
# astr.count('l', 3, 12)
# astr.endswith('!')
# astr.endswith('o', 3, 12)
# astr.startswith('e', 1, 10)
# astr.islower()
# astr.isdigit()
# astr.isalnum()
# astr.upper()
# astr.strip()
# astr.lstrip()
# astr.rstrip()
# astr.upper()
# astr.lower()
# "192.168.1.1".split('.')
# '.'.join(['hello', 'world', '2018'])
##########################################################
# alist=[10,2,3,'bob','tom']
# alist[0]=10
# alist[1:3]=[20,30]
# alist[2:2]=[22,24,26,28]
# alist.pop()
# alist.pop(3)
# alist.pop(alist.index('bob'))
# alist.sort()
# alist.append(40)
# alist.extend('new')
# alist.extend(['hello','world','2018'])
# alist.remove(20)
# alist.index('bob')
# blist=alist.copy()
# alist.insert(1,'alice')
# alist.reverse()
# alist.count(30)
# alist.clear()
###############################################################
import os

title = '''这是一个栈，拥有如下功能：
1.压栈
2.出栈
3.查询
请输入1/2/3选择你想使用的功能，输入end结束：'''
alist = []

def read_list():
    if not os.path.exists('/tmp/alist'):
        os.mknod('/tmp/alist')
    with open('/tmp/alist','r') as f:
        data=True
        while data:
            data=f.readline().rstrip('\n')
            alist.append(data)
    return alist


def in_stacks():
    num = input('\033[31;1m请输入你要加入的值：\033[0m')
    alist.append(num)
    print('\033[32;1m%s压栈成功\033[0m' % num)


def out_stacks():
    if alist:
        result = alist.pop()
        print('\033[32;1m%s出栈成功\033[0m' % result)
    else:
        print('\033[31;1m空栈\033[0m')


def select_stacks():
    word = input('\033[31;1m请输入你要查询的值：\033[0m')
    if word == '':
        print(alist)
    else:
        if word in alist:
            print('\033[32;1m%s共有%s个，分别在：\033[0m' % (word, alist.count(word)))
            for index, value in enumerate(alist):
                if value == word:
                    print('\033[32;1m栈的第%s位\033[0m' % index + 1)
        else:
            print('\033[33;1m未查询到\033[0m')


def save_stacks():
    print('\033[32;1m保存数据中，请稍后\033[0m')
    with open('/tmp/alist', 'w')as f:
        for i in alist:
            f.writelines(str(i) + '\n')


if __name__ == '__main__':
    alist=read_list()
    while True:
        choice = input(title).strip()
        if choice == 'end':
            save_stacks()
            break
        elif choice not in '123':
            print('\033[31;1m输入错误，请重新输入\033[0m')
            continue
        cmds = {'1': in_stacks, '2': out_stacks, '3': select_stacks}
        cmds[choice]()
