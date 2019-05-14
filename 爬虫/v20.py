'''
爬取豆瓣电影数据
了解ajax的基本爬取方式
'''

from urllib import request

import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=40&limit=20"

req = request.urlopen(url)

rsp = req.read().decode()

html = json.loads(rsp)
print(html)