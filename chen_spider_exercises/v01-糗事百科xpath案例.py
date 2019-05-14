'''
爬取糗事百科，页面自己来找
分析：
1. 需要用到requests爬取页面，用xpath、re来提取数字
2. 可提取信息谁用户头像链接，段子内容，点赞，好评次数
3. 保存到json文件中

大致分三部分
1. down下页面
2. 利用xpath提取信息
3. 保存文件落地
'''

import requests
from lxml import etree

url = "https://www.qiushibaike.com/text/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}

# 下载页面
rsp = requests.get(url, headers=headers)

html = rsp.text
#print(html)
# 把页面解析成html
html = etree.HTML(html)
print(html.text)

