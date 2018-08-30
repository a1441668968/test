import requests
from urllib import request
import hashlib
import os
import tarfile


def get_web(url):
    r = requests.get(url=url)
    return r.text


def download(url, fname):
    html = request.urlopen(url=url)
    with open(fname, 'wb')as f:
        while True:
            data = html.read(1024)
            if not data:
                break
            f.write(data)


def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb')as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def deploy(soft):
    os.chdir('/var/www/html/deploy/packages/')
    tar = tarfile.open(soft, 'r:gz')
    tar.extractall()
    tar.close()


if __name__ == '__main__':
    ver = get_web('http://192.168.1.161/deploy/packages/live_version').strip()
    soft_name = 'myproject%s.tar.gz' % ver
    soft_url = 'http://192.168.1.161/deploy/packages/' + soft_name
    soft_path = os.path.join('/var/www/html/packages/', soft_name)
    download(soft_url, soft_path)
    local_md5 = check_md5(soft_path)
    get_md5 = get_web(soft_url + '.md5').strip()
    if local_md5 == get_md5:
        deploy(soft_path)
