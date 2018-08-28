import urllib.request
html=urllib.request.urlopen('http://www.baidu.com/')
print(html.readline())
print(html.read(4096))
print(html.readlines())