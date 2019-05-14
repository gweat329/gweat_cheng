'''
处理js加密代码
v2
'''


'''
通过查找，能找到js代码中操作代码
1.这个是计算salt的公式 salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2. sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，
第二个参数就是输入的要查找的单词     
'''

def getSalt():
    '''
    salt公式："" + (new Date).getTime() + parseInt(10 * Math.random(), 10)
    把它翻译成Python代码
    :return:
    '''

    import time, random

    salt = int(time.time()*1000) + random.randint(0, 10)

    return salt

def getMd5(v):
    import hashlib

    md5 = hashlib.md5()

    # update需要一个bytes格式的参数
    md5.update(v.encode("utf-8"))

    sign = md5.hexdigest()

    return sign

def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "@6f#X3=cCuncYssPsuRUE"

    sign = getMd5(sign)

    return sign

from urllib import request, parse

def youdao(key):
    import time

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getSign(key, salt),
        # "ts" = "" + (new Date).getTime()
        "ts": int(salt*0.1),
        "bv": "1de9313c44872e4c200c577f99d4c09e",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    print(data)

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Host": "fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0(X11Ubuntu;Linux x86_64;rv: 66.0)Gecko/20100101Firefox/66.0",
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q =0.5,en-US;q=0.3,en;q=0.2",
        # "Accept-Encoding": "gzip,deflate",
        "Referer": "http://fanyi.youdao.com/",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": len(data),
        "Connection": "keep- alive",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1154903484.9473486;OUTFOX_SEARCH_USER_ID = -1390206993@10.169.0.102;YOUDAO_MOBILE_ACCESS_TYPE = 1;JSESSIONID = aaayL0ckp9R0p9spIebQw;___rl__test__cookies = 1556943641021"
    }

    req = request.Request(url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao("gweat")

