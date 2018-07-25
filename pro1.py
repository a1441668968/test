#!/usr/local/bin/python3
import sys
import os


def ls(*args):
    m = os.listdir(*args)
    print(m)
    for l in m:
        if os.path.isdir(l):
            return ls(l)


if __name__ == '__main__':
    ls(sys.argv[1])
