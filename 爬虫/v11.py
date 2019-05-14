from urllib import request, error

if __name__ == '__main__':

    url = 'http://www.renren.com/895930752/profile'

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)