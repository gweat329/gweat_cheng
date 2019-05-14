'''
构建代理群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用random.choice


分析步骤
1. 构建代理群
2.每次访问，随机选取代理并执行
'''

from urllib import request, error

# 使用代理步骤
# 1. 设置代理地址
proxy_list = [
    {"http":"61.178.238.122:63000"},
    {"http":"47.94.57.119:80"},
    {"http":"61.63.110.221:32478"},
    {"http":"122.143.169.182:8080"}
]

# 创建代理处理器ProxyHandler

proxy_handler_list = []

for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 创建opener

opener_list = []

for opener in proxy_handler_list:
    opener = request.build_opener(opener)
    opener_list.append(opener)


import random
url = "https://www.baidu.com"

try:
    # 安装opener之前先要从opener_list中随机抽取一个
    opener = random.choice(opener_list)
    # 安装opener
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.HTTPError as e:
    print("HTTP错误：",e)
except error.URLError as e:
    print("URL错误：",e)
except Exception as e:
    print(e)
