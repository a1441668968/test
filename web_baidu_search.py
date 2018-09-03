import requests

r = requests.get('https://www.baidu.com/s', params={'wd': 'python'})
with open('/tmp/bd.html', 'wb')as f:
    f.write(r.content)
