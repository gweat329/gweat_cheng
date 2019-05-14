'''
requests proxy:代理用法

'''
import requests

proxies = {
    "http": "121.69.10.62:9090",
    "https":"121.69.10.62:9090"
}


data = {
    "kw": "girl"

}
headers = {
    "Content-Length": str(len(data)),
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"
}
rsp = requests.request("post", "https://fanyi.baidu.com/sug", proxies=proxies, data=data, headers=headers)

print(rsp.json())