# adict=dict()
# print(dict(['ab','cd']))
# bdict=dict([('name','bob'),('age',25)])
# cdict = {}.fromkeys(['zhang3', 'li4', 'wang5'], 20)
# for key in cdict:
#     print('%s:%s' % (key, cdict[key]))
# print('%(name)s:%(age)s'%bdict)
# bdict['name']='jack'
# bdict['email']='abc@123.com'
# len(bdict)
# bdict.keys()
# bdict.values()
# bdict.items()
# bdict.get('name')
# bdict.get('qq','not found')
# bdict.get('age','not found')
# bdict.update({'tel':'123456789'})
# adict = bdict.copy()
# bdict.setdefault('add', 'china')
###############################################################
# userdb = {}
#
#
# def register():
#     username = input('注册的用户名：')
#     if username in userdb:
#         print('%s已存在' % username)
#     else:
#         password = input('请输入密码：')
#         userdb[username] = password
#
#
# def login():
#     username = input('请输入用户名')
#     password = input('请输入密码')
#     if userdb.get(username) != password:
#         print('用户名或密码错误')
#     else:
#         print('登录成功')
#
#
# def show_menu():
#     promt = '''1.注册
# 2.登录
# 3.退出
# 请在1/2/3中选择：'''
#     cmds = {'1': register, '2': login}
#     while True:
#         choice = input(promt).strip()[0]
#         if choice not in '123':
#             print('输入错误，请重新输入')
#             continue
#         elif choice == '3':
#             break
#         else:
#             cmds[choice]()
#
#
# if __name__ == '__main__':
#     show_menu()
############################################################
# import sys
#
#
# def u2d(fname):
#     dst_fname = fname + '.txt'
#     with open(fname)as s_f:
#         with open(dst_fname, 'w')as d_f:
#             for line in s_f:
#                 line = line.rstrip() + '\r\n'
#                 d_f.write(line)
#
#
# if __name__ == '__main__':
#     u2d(sys.argv[1])
#######################################################
# import time
#
# length = 19
# count = 0
# try:
#     while True:
#         print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
#         time.sleep(0.2)
#         count = (count + 1) % 20
# except KeyboardInterrupt:
#     print('\ngame over')
##########################################################
# aset = set('abcd')
# bset = set('defg')
# cset = aset | bset
# aset.union(bset)
# aset & bset
# aset.intersection(bset)
# aset - bset
# aset.difference(bset)
# aset.issubset(cset)
# cset.issuperset(aset)
# aset.add('new')
# aset.update(['aaa', 'bbb'])
# aset.remove('bbb')
##############################################################
# with open('passwd') as f:
#     aset = set(f)
# with open('mima') as f:
#     bset = set(f)
# with open('diff', 'w') as f:
#     f.writelines(aset - bset)
################################################################
# import time
# time.localtime()
# time.gmtime()
# time.time()
# time.mktime(time.localtime())
# time.sleep(1)
# time.asctime()
# time.ctime()
# time.strftime('%Y-%m-%d')
# time.strftime('%H-%M-%S')
# time.strptime('2018-07-20','%Y-%m-%d')
# import datetime
# dt=datetime.datetime.today()
# datetime.datetime.now()
# datetime.datetime.strptime('2018/7/20','%Y/%m/%d')
# datetime.datetime.strptime('2018~7~20','%Y~%m~%d')
# datetime.datetime.ctime(dt)
# datetime.datetime.strftime(dt,'%Y%m%d')
# dt+datetime.timedelta(days=10,hours=3)
####################################################################
# try:
#     n = int(input('输入一个数：'))
#     result=100/n
# except (ValueError,ZeroDivisionError):
#     print('无效的数字')
# except (KeyboardInterrupt, EOFError):
#     print('byebye')
# else:
#     print(result)
# finally:
#     print('over')
####################################################
# def set_age(name, age):
#     if not 0 < age < 150:
#         raise ValueError('超过范围')
#     print('%s is %s' % (name, age))
#
#
# def set_age2(name, age):
#     assert 0 < age < 150, '超过范围'
#     print('%s is %s' % (name, age))
#
#
# if __name__ == '__main__':
#     set_age('zhang3', 30)
#     set_age2('lisi', 20)
###################################################
# import os
# os.getcwd()
# os.listdir()
# os.listdir('/tmp')
# os.mkdir('/tmp/a')
# os.chdir('/tmp/a')
# os.mknod('test')
# os.symlink('/etc/passwd','link')
# os.path.isfile('test')
# os.path.islink('link')
# os.path.isdir('/tmp')
# os.path.exists('/tmp')
# os.path.basename('/ttt/aaa/bbb')
# os.path.dirname('/ttt/aaa/bbb')
# os.path.split('/ttt/aaa/bbb')
# os.path.join('/ttt/aaa', 'bbb')
# os.path.abspath('test')
########################################################3
# import pickle
#
# first_list = ['a', 'b', 2]
# with open('/tmp/listdata', 'wb')as f:
#     pickle.dump(first_list, f)
# with open('/tmp/listdata', 'rb')as f:
#     new_list = pickle.load(f)
# print(new_list)
#######################################################
import pickle
import os
import time

title = '''1.开销
2.收入
3.结束
请在1/2/3中选择:'''


def load_money():
    if os.path.exists('money'):
        with open('money', 'rb') as f:
            money = pickle.load(f)
    else:
        money = 10000.0
    return money


def use_money(money):
    num = float(input('请输入开销的金额:'))
    money -= num
    node = note()
    atime = time.strftime('%Y.%m.%d')
    astr='%-12s\t%-8s\t%-8s\t%-10s\t%-20s\n'%(atime,num,'',money,node)
    save_node(astr)
    return money


def get_money(money):
    num = float(input('请输入收入的金额:'))
    money += num
    node = note()
    atime = time.strftime('%Y.%m.%d')
    astr='%-12s\t%-8s\t%-8s\t%-10s\t%-20s\n'%(atime,'',num,money,node)
    save_node(astr)
    return money


def save_node(astr):
    if not os.path.exists('node'):
        with open('node','w') as f:
            f.write('%-12s\t%-8s\t%-8s\t%-10s\t%-20s\n'%('时间','支出','收入','余额','说明'))
    with open('node', 'a') as f:
        f.write(astr)


def note():
    node = input('请输入说明')
    return node


def save_money(money):
    print('保存记录中')
    with open('money', 'wb') as f:
        pickle.dump(money, f)


if __name__ == '__main__':
    money = load_money()
    cmds = {'1': use_money, '2': get_money}
    while True:
        print('当前拥有%8.1f'% money)
        choice = input(title).strip()
        if choice == '3':
            save_money(money)
            break
        elif choice not in '123':
            print('输入错误,请重新输入')
            continue
        else:
            money=cmds[choice](money)
