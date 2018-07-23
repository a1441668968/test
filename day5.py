#!/usr/local/bin/python3
# def use_node(name, age):
#     print('%s is %s' % (name, age))
#
#
# use_node('bob', 25)
# use_node(name='bob', age=25)
# use_node('bob', age=25)
#
#
# def fun1(*args):
#     print(args)
#
#
# def fun2(**kwargs):
#     print(kwargs)
#
#
# def fun3(x, y):
#     print(x * y)
#
#
# fun1()
# fun1(10)
# fun1('bob', 20)
# fun2()
# fun2(name='bob', age=20)
# fun3(*[10, 5])
# use_node(**{'name': 'bob', 'age': 25})
################################################
# import random
#
#
# def add_num(x, y):
#     return x + y
#
#
# def sub_num(x, y):
#     return x - y
#
#
# def exam():
#     cmds = {'+': add_num, '-': sub_num}
#     print('游戏开始\n')
#     num = [random.randint(1, 100) for i in range(2)]
#     num.sort(reverse=True)
#     op = random.choice('+-')
#     result = cmds[op](*num)
#     jihui = 3
#     while True:
#         try:
#             answer = int(input('请计算%d%s%s=' % (num[0], op, num[1])))
#         except ValueError:
#             continue
#         except (KeyboardInterrupt, EOFError):
#             print('请认真答题')
#         else:
#             jihui -= 1
#             if result == answer:
#                 print('回答正确')
#                 break
#             else:
#                 if not jihui:
#                     print('正确答案是%d' % result)
#                     break
#                 else:
#                     print('回答错误，还有%d次机会' % jihui)
#                     continue
#
#
# if __name__ == '__main__':
#     while True:
#         exam()
#         try:
#             yn = input('是否继续，y/n:').strip()[0]
#         except (KeyboardInterrupt, EOFError):
#             print('\nbyebye')
#             yn = 'n'
#         except IndexError:
#             continue
#         if yn in 'nN':
#             break
##############################################################################
# import random
#
# a = lambda x, y: x + y
# print(a(3, 4))
# alist = [random.randint(1, 100) for i in range(10)]
# print(alist)
# result = filter(lambda x: x % 2, alist)
# print(list(result))
# result2 = map(lambda x: x * 2 + 1, alist)
# print(list(result2))
#################################################################################
# import functools
#
#
# def foo(a, b, c, d, e):
#     return a + b + c + d + e
#
#
# add = functools.partial(foo, a=1, b=2, c=3, d=4)
# add1 = functools.partial(foo, *[1, 2, 3, 4])
# add2 = functools.partial(foo, **{'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(add(e=5))
# print(add1(5))
# print(add2(e=5))
##############################################################################
# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n - 1)
#
# print(factorial(6))
########################################################################
# import random
#
#
# def quick_sort(num):
#     if len(num) < 2:
#         return num
#     middle = num[0]
#     small = list()
#     large = list()
#     for i in num[1:]:
#         if i < middle:
#             small.append(i)
#         else:
#             large.append(i)
#     return quick_sort(small) + [middle] + quick_sort(large)
#
#
# alist = [random.randint(1, 100) for i in range(10)]
# print(alist)
# print(quick_sort(alist))
#######################################################################
# def mygen():
#     yield 'hello'
#     a = 10 + 20
#     yield a
#     yield [1, 2, 3]
#
# for i in mygen():
#     print(i)
#################################################
# def block(f):
#     block = []
#     counter = 10
#     for line in f:
#         block.append(line)
#         counter -= 1
#         if not counter:
#             yield block
#             block = []
#             counter = 10
#     if block:
#         yield block
#
#
# if __name__ == '__main__':
#     f = open('/tmp/passwd')
#     for line in block(f):
#         print(line)
#     f.close()
##################################################
# def colour(func):
#     def red(*args):
#         return '\033[031;1m%s\033[0m' % func(*args)
#     return red
#
#
# @colour
# def hello(word):
#     return 'hello %s' % word
#
#
# def welcome():
#     return 'welcome'
#
#
# print(hello('world'))
# print(colour(welcome)())
# print(hello(welcome()))
######################################################
import time


def count_time(func):
    start_time = time.time()

    def ct(*args):
        func(*args)
        end_time = time.time()
        return end_time - start_time

    return ct


def func1():
    time.sleep(1)


def func2():
    time.sleep(2)


if __name__ == '__main__':
    print(count_time(func1)())
    print(count_time(func2)())
