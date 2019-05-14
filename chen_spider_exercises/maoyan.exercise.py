'''
利用正则来爬取猫眼电影
1. url:http://maoyan.com/board
2. 把电影信息尽可能多的拿出来

分析
1. 一个影片的内容是以dd开头的单元
2. 再单元内存在一部电影的所有信息

思路：
1. 利用re把dd内容都给我找到
2. 对应找到的每一个dd，用re挨个查找需要的信息

方法就是三步走：
1. 把页面down下来
2. 提取出dd单元为单位的内容
3. 对每一个dd，进行单独信息提取
'''

from urllib import request

url = "http://maoyan.com/board"

rsp = request.urlopen(url)

html = rsp.read().decode()

#print(html)

import re

s = r'<dd>(.*?)</dd>'

pattern = re.compile(s, re.S)

films = pattern.findall(html)
print(len(films))

for film in films:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)