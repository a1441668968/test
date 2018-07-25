#!/usr/local/bin/python3
import tarfile
import sys
import os
import hashlib
import pickle
import time


class BackUp:
    def __init__(self, path):
        self.path = path

    def full_backup(self):
        file_md5 = {}
        fullfile = os.path.basename(self.path) + 'full' + time.strftime('%Y%m%d')+'.tar.gz'
        with tarfile.open(fullfile,'w:gz')as tar:
            for file in os.listdir(self.path):
                tar.add(file)
                file_md5.update({file: hashlib.md5(file)})
        with open('md5.node', 'wb')as f:
            pickle.dump(file_md5, f)

    def extra_backup(self):
        with open('md5.node', 'rb')as f:
            file_md5 = pickle.load(f)
        newfile = os.path.basename(self.path) + time.strftime('%Y%m%d')+'.tar.gz'
        with tarfile.open(newfile,'w:gz')as tar:
            for file in os.listdir(self.path):
                if file_md5.get(file) != hashlib.md5(file):
                    tar.add(file)
                    file_md5.update({file: hashlib.md5(file)})
        with open('md5.node', 'wb')as f:
            pickle.dump(file_md5, f)


if __name__ == '__main__':
    b = BackUp('/tmp/a')
    if time.strftime('%a') == 'Wed':
        b.full_backup()
    else:
        b.extra_backup()
