import requests
# 创建session对象，可以保持cookie值
ss = requests.session()

headers = {"User-Agent": "xxxxxxxxx"}

data = {"name": "xxxxxxxxxxx"}

# 此时，由创建的session管理请求，负责发出请求，
ss.post("http://www.baidu.com", data=data, headers=headers)

rsp = ss.get("xxxxxxxxx")