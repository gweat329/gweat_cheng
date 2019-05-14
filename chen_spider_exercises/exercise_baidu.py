'''
随意爬取一个贴吧
https://tieba.baidu.com/f?kw=厚涂&ie=utf-8&pn=0
提取10页的url,顺便创建10个xxx.html文档
'''

from urllib import parse, request

if __name__ == '__main__':

    qs = {
        "kw": "厚涂",
        "ie": "utf-8",
        "pn": 0

    }
    baseurl = "https://tieba.baidu.com/f?"

    urls = []

    for i in range(10):
        pn = i * 50
        qs["pn"] = str(pn)
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    num = 1
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")

        #print(html)
        with open("houtu{0}.html".format(num), "w") as f:

            f.write(html)
        num += 1
        #print(rsp)


