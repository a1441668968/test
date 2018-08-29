import json
from urllib import request

adict = {'name': '张三', 'age': 25}
print(json.dumps(adict))
print(json.loads(json.dumps(adict)))
weather = request.urlopen('http://www.weather.com.cn/data/sk/101210101.html')
info = request.urlopen('http://www.weather.com.cn/data/cityinfo/101210101.html')
zs = request.urlopen('http://www.weather.com.cn/data/zs/101210101.html')
weather_data = weather.read()
print(json.loads(weather_data))
print('#' * 100)
info_data = info.read()
print(json.loads(info_data))
print('#' * 100)
zs_data = zs.read()
print(json.loads(zs_data))
