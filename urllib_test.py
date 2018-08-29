from urllib import request, error
import os
import re

html = request.urlopen('http://www.baidu.com/')
print(html.readline())
print(html.read(4096))
print(html.readlines())


def download(url, fname):
    header = {'User-Agent': '"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"'}
    r = request.Request(url, headers=header)
    try:
        html = request.urlopen(r)
    except error.HTTPError as e:
        print(e)
    else:
        with open(fname, 'wb')as f:
            while True:
                data = html.read(4096)
                if not data:
                    break
                f.write(data)


def search_url(fname, patt):
    patt_list = []
    cpatt = re.compile(patt)
    with open(fname) as f:
        for line in f:
            m = cpatt.search(line)
            if m:
                item = m.group()
                patt_list.append(item)
    return patt_list


if __name__ == '__main__':
    download('https://www.baidu.com/', '/tmp/baidu.html')
    download(
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535435104365&di=479f195cd21bfc3ef8becca251976d43&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D2326766919%2C2993649423%26fm%3D214%26gp%3D0.jpg',
        '/tmp/girl.jpg')
    r = request.quote('你好')
    print(r)
    ur = request.unquote(r)
    print(ur)
    img_dirs = '/tmp/imgs'
    if not os.path.exists(img_dirs):
        os.mkdir(img_dirs)
    photo = '/tmp/photo'
    download('http://www.tmooc.cn/', photo)
    img_patt = 'http://[\w./]+\.(jpg|jpeg|gif|png)'
    img_list = search_url(photo, img_patt)
    print(img_list)
    for url in img_list:
        fname = url.split('/')[-1]
        fname = os.path.join(img_dirs, fname)
        download(url, fname)
