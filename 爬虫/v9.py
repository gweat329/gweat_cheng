'''
访问一个网址
更改自己的UserAgent进行伪装
'''
from urllib import request, error

if __name__ == '__main__':

    url = "https://www.baidu.com"

    try:
        # 使用headers方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
        # req = request.Request(url, headers=headers)


        # 使用add_header的方法
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)")


        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("DONE..............")