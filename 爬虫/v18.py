'''
破解有道词典
v1
'''


from urllib import request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i":key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15569436410365",
        "sign":"44c14e80d740213eb70d4cd9cf053287",
        "ts":"1556943641036",
        "bv":"1de9313c44872e4c200c577f99d4c09e",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }

    data = parse.urlencode(data).encode()

    headers = {
        "Host": "fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0(X11Ubuntu;Linux x86_64;rv: 66.0)Gecko/20100101Firefox/66.0",
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q =0.5,en-US;q=0.3,en;q=0.2",
        #"Accept-Encoding": "gzip,deflate",
        "Referer": "http://fanyi.youdao.com/",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "236",
        "Connection": "keep- alive",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1154903484.9473486;OUTFOX_SEARCH_USER_ID = -1390206993@10.169.0.102;YOUDAO_MOBILE_ACCESS_TYPE = 1;JSESSIONID = aaayL0ckp9R0p9spIebQw;___rl__test__cookies = 1556943641021"
    }

    req = request.Request(url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("girl")