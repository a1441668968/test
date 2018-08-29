import requests

payload = {'wd': 'centos7'}
r1 = requests.get('https://www.baidu.com/s', params=payload)
header = {'User-Agent': '"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"'}
r2 = requests.get(url='https://www.baidu.com/', headers=header)
# data = {'username': 'lili', 'password': '123456'}
# r3 = requests.post(url='127.0.0.1', data=data)
r4 = requests.get('https://www.baidu.com')
print(r4.text)
print(r4.encoding)
r4.encoding = 'utf8'
print(r4.text)
print(r4.cookies)
r5 = requests.get('https://pic.feizl.com/upload/allimg/170808/813cooff2o0b24.jpg')
with open('/tmp/a.jpg', 'wb')as f:
    f.write(r5.content)
r6 = requests.get('http://www.weather.com.cn/data/sk/101210101.html')
r6.encoding = 'utf8'
print(r6.json())
print(r6.status_code)
if r6.status_code == requests.codes.ok:
    print('ok')
print(r6.headers)
