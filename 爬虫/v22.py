'''
使用参数headers和params
研究返回结果
'''

import requests

# 完整访问url是下面加上参数构成
url = "https://www.baidu.com/s?"

kw = {
    "wd": "王八蛋"
}

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"

}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)