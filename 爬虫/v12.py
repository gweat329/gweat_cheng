from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/895930752/profile"

    headers = {
        "cookie": "anonymid=jv4wq53i-hutg1x; depovince=GW; jebecookies=cc1b959e-aaa2-4f22-a06d-97f5765799ff|||||; _r01_=1; JSESSIONID=abcvr8XDm70e_bDSVuYPw; ick_login=b1691a78-cd9c-42e3-a810-6c72705ac28d; jebe_key=7590d9ac-44db-4e55-a979-17010392be71%7C224032297e97e0244d7b529732d20b9e%7C1556696260337%7C1%7C1556696260244; t=dd930a2512677eabb70020f95c7fecef2; societyguester=dd930a2512677eabb70020f95c7fecef2; id=895930752; xnsid=8dac2cfc; ver=7.0; loginfrom=null; wp_fold=0"

    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

    with open("rsp.html", "w") as f:
        f.write(html)

