'''
使用代理访问百度网站
'''


from urllib import request, error


if __name__ == '__main__':

    url = "http://www.baidu.com"

    # 使用代理步骤
    # 1. 设置代理地址
    proxy = {'http': '120.194.18.90:81'}

    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler()

    # 创建Opener
    opener = request.build_opener(proxy_handler)

    # 安装Opener

    request.install_opener(opener)

    #现在如果访问url，则使用代理服务器

    try:

        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)