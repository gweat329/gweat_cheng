'''
爬取58同城数据
1. 需要登录，登录地址 login_url = "http://passport.58.com/58/login/pc/dologin"
w = function(e) {
        var t = 1411093327735 - new Date().getTime(), n = new Date().getTime() + t;
        return encryptString(n + encodeURIComponent(e), p.rsaExponent, p.rsaModulus);
'''

from urllib import parse, error, request

from http import cookiejar

import json

def login():

    login_url = "http://passport.58.com/58/login/pc/dologin"

    data = {
        "username": "gweat329",
        "password": "707909078f87b45aa664591a1901625ba15400ea4ac91a8a0fb6ecc87dbb1294f4e294c5b3a5f57f395310b0371367672a0d5f548487fe671071a15bc382cb9866c5dda03be2a715c9dd811666714869b7bb6b25bd5b12dac2ecda3192c361b44451b16f25cbf41736b567ce437e6c8f6695686b7804894dd91b2dd3e36b6385",
        "fingerprint": "NzKMrMCut4BeOMt0kF1fCeF2m_gm-gLn",
        "callback": "successFun",
        "token": "hxf0vp9ivOjNWAp2czg6GOFsAIe8FiZV",
        "source": "58-default-pc",
        "path": "https%3A%2F%2Fwh.58.com%2F%3Fpts%3D1557475516428",
        "domain": "58.com",
        "finger2": "zh-CN|24|1|4|1366_768|1299_741|-480|1|1|1|undefined|undefined|unknown|Linux",
        "psdk-d": "jsdk",
        "psdk-v": "1.0.0"
    }

    headers = {
        "Host": "passport.58.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://passport.58.com/login/?path=https%3A//wh.58.com/&PGTID=0d100000-0009-edcb-b00f-a62b0d78da0d&ClickID=2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": len(data),
        "Connection": "keep-alive",
        #"Cookie": "58home=wh; id58=c5/njVzVHSEKW46eAyYkAg==; city=wh; 58tj_uuid=47345ffc-ffb7-489d-8706-4915075d259a; new_session=1; new_uv=1; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253Ds7gvFQHJlUM8AU57tCeR3fOCp5UFqCA5iyYH6lFxv4u%2526wd%253D%2526eqid%253Da393001900004208000000055cd51d1c; als=0; ppStore_fingerprint=4B1708A666D99535DA1C9EA8B24188572F897C40B1C0FB4D; finger_session=NzKMrMCut4BeOMt0kF1fCeF2m_gm-gLn; xxzl_deviceid=mUBgb7V5YnX3Rv1jagzZ2GTj9Q0snQpFczwIRQZVYy%2BewrHdJRGxVAIK1JaIG218",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers"
    }
    data = parse.urlencode(data).encode("utf-8")
    print(data["password"])

    f = r"58city_cookie.txt"

    cookie_handler = cookiejar.MozillaCookieJar(f)

    http_handler = request.HTTPCookieProcessor(cookie_handler)

    opener = request.build_opener(http_handler)

    req = request.Request(login_url, data=data, headers=headers)

    try:
        rsp = opener.open(req)

        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)

        html = rsp.read().decode("utf-8")
        print(html)
        print(type(html))
    except Exception as e:
        print(e)
if __name__ == '__main__':
    login()