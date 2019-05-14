from urllib import request
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':

    url = "http://www.sohu.com/a/309692833_209689?scm=1002.590044.0.0&spm=smpc.ch12-read.fd-news.1.15564262279475BGvlEB"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))

    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode("utf-8")
    print(html)