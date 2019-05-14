'''
登录开心网
利用cookie
免除ssl
'''
from urllib import request, parse

import ssl
# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

from http import cookiejar

cookie = cookiejar.CookieJar()
cookiejar_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookiejar_handler)

'''
步骤：
1. 寻找登录入口，通过搜查相应文字可以快速定位
login_url = "https://security.kaixin001.com/login/login_post.php"
url = "http://www.kaixin001.com/home/?_profileuid=181852766"
'''


def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "loginemail": "15871686594",
        "password": "123456"
    }

    # 对post的data数据进行编码
    data = parse.urlencode(data)

    # 协议的请求头
    headers = {
        "Content-Length":len(data),
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"

    }

    # 构造请求Request对象
    # data要求是一个bytes对象，所以要进行编码
    req = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(req)

    html = rsp.read().decode()

def getHomePage():

    base_url = "http://www.kaixin001.com/home/?_profileuid=181852766"

    rsp = opener.open(base_url)
    html = rsp.read().decode()
    #print(html)
    with open("new.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()
