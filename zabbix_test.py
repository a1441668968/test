import requests
import json

url = 'http://192.168.1.53/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": {},
    "id": 1,
    "auth": None
}
r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r.json())

data1 = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
}
r1 = requests.post(url=url, headers=headers, data=json.dumps(data1))
print(r1.json())

data2 = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                "Zabbix server"
            ]
        }
    },
    "auth": "9ba4de5941d8dfa149e3ec896e7a41be",
    "id": 2
}
r2 = requests.post(url=url, headers=headers, data=json.dumps(data2))
print(r2.json())

data3 = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Zabbix servers",
                "Linux servers",
                "Templates"
            ]
        }
    },
    "auth": "9ba4de5941d8dfa149e3ec896e7a41be",
    "id": 3
}
r3 = requests.post(url=url, headers=headers, data=json.dumps(data3))
for item in r3.json()['result']:
    print(item['groupid'], item['name'], sep=':')

data4 = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
    },
    "auth": "9ba4de5941d8dfa149e3ec896e7a41be",
    "id": 4
}
r4 = requests.post(url=url, headers=headers, data=json.dumps(data4))
for item in r4.json()['result']:
    print(item['templateid'], item['host'], sep=':')

data5 = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "My server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.53",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "1"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
    },
    "auth": "9ba4de5941d8dfa149e3ec896e7a41be",
    "id": 5
}
r5 = requests.post(url=url, headers=headers, data=json.dumps(data5))
