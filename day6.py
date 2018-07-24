#!/usr/local/bin/python3
# import hashlib
# import sys
#
#
# def check_md5(fname):
#     with open(fname, 'rb') as f:
#         m = hashlib.md5()
#         while True:
#             data = f.read(4096)
#             if not data:
#                 break
#             # for data in f.readlines():
#             m.update(data)
#
#     return m.hexdigest()
#
#
# print(check_md5(sys.argv[1]))
############################################
# import tarfile
#
# tar = tarfile.open('/tmp/test.tar.gz', 'w:gz')
# tar.add('/etc/hosts')
# tar.add('/etc/passwd')
# tar.close()
# tar = tarfile.open('/tmp/test.tar.gz', 'r:gz')
# tar.extractall()
# tar.close()
###############################################
# class BearToy:
#     def __init__(self, bear_name, colour, size):
#         self.name = bear_name
#         self.colour = colour
#         self.size = size
#
#     def sing(self):
#         print('lala')
#         print('my name is %s' % self.name)
#
#
# tidy = BearToy('Tidy', 'write', 'large')
# tidy.sing()
####################################################
# class Hotel:
#     def __init__(self, price=200, cut_off=1.0,breakfast=15):
#         self.price = price
#         self.cut_off = cut_off
#         self.bf=breakfast
#
#     def pay(self, days=1):
#         return (self.price * self.cut_off+self.bf) * days
#
#
# stdroom = Hotel()
# bigroom = Hotel(280, 0.8)
# print(stdroom.pay(5))
# print(bigroom.pay(2))
####################################################
# import time
#
#
# class Contact:
#     def __init__(self, phone, email):
#         self.phone = phone
#         self.email = email
#
#     def call(self):
#         print(self.phone)
#
#
# class BearToy:
#     def __init__(self, colour, size, phone, email):
#         self.colour = colour
#         self.size = size
#         self.vendor = Contact(phone, email)
#
#
# class NewBear(BearToy):
#     def run(self):
#         print('running...')
#
#
# class UpdateBear(BearToy):
#     def __init__(self, colour, size, phone, email, date):
#         super(UpdateBear, self).__init__(colour, size, phone, email)
#         self.date = date
#
#     def test(self):
#         print('running')
#
#
# bigbear = BearToy('write', 'big', 12345, 'bear@qq.com')
# bigbear.vendor.call()
# newbear = NewBear('write', 'big', 12345, 'bear@qq.com')
# newbear.run()
# big_new_bear = UpdateBear('black', 'large', 56789, 'hello@qq.com', time.localtime())
# big_new_bear.vendor.call()
# big_new_bear.test()
#####################################################################
# class A:
#     def foo(self):
#         print('A')
#
#
# class B:
#     def foo(self):
#         print('B+')
#     def bar(self):
#         print('B')
#
#
# class C(A, B):
#     def foo(self):
#         print('C')
#
#
# C().foo()
# C().bar()
###############################################################
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def create(cls, dstr):
#         y, m, d = map(int, dstr.split('-'))
#         dt = cls(y, m, d)
#         return dt
#
#     @staticmethod
#     def is_date_valid(dstr):
#         y, m, d = map(int, dstr.split('-'))
#         return 1 <= d <= 31 and 1 <= m <= 12 and y < 4000
#
#
# day = Date.create('2018-7-5')
# birth_day = Date(2000, 5, 6)
# print(day.year)
# print(birth_day.year)
# print(Date.is_date_valid('2018-7-23'))
############################################################
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return 'book name is %s' % self.title
#
#     def __call__(self, *args, **kwargs):
#         print('%s is written by %s' % (self.title, self.author))
#
#
# my_book = Book('hello world', 'zhang3')
# print(my_book)
# my_book()
#############################################################
# class Transformation:
#     def __init__(self, fname, diff):
#         self.fname = fname
#         self.diff = diff
#         dst_fname = self.fname + '.txt'
#         with open(self.fname, 'r')as f:
#             with open(dst_fname, 'w') as d_f:
#                 for line in f:
#                     line = line.rstrip() + self.diff
#                     d_f.write(line)
#
#
# class to_windows(Transformation):
#     def run(self,):
#         pass
#
#
# class to_linux(Transformation):
#     def run(self):
#         pass
#
#
# if __name__ == '__main__':
#     prompt = '''请选择：
# 1.linux转windows
# 2.windows转linux:'''
#     fnote = '''请输入转化的文件：'''
#     choice = int(input(prompt))
#     fname = input(fnote)
#     if choice == 1:
#         to_windows(fname, '\r\n')
#     elif choice == 2:
#         to_linux(fname, '\n')
#     else:
#         print('输入错误')
##############################################################
import os


class Convert:
    def __init__(self):
        self.fname = fname

    def to_linux(self):
        dst_name = os.path.splitext(self.fname)[0] + '.linux'
        with open(self.fname)as f:
            with open(dst_fname, 'w') as d_f:
                for line in f:
                    line = line.rstrip() + '\n'
                    d_f.write(line)


def to_window(self):
    dst_name = os.path.splitext(self.fname)[0] + '.windowd'
    with open(self.fname)as f:
        with open(dst_fname, 'w') as d_f:
            for line in f:
                line = line.rstrip() + '\r\n'
                d_f.write(line)


if __name__ == '__main__':
    c = Convert('/tmp/passwd')
    c.to_linux()
    c.to_window()
