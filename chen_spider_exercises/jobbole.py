'''
爬取伯乐在线的美女联系方式
需要：
1. 登录
2. 再登录和相应声望值的前提下，提取对方的邮箱
'''

from urllib import request, parse, error
from http import cookiejar
import json
data = {
    "p_skey":"4AzXUe1XjgXP4Uzv17xfIxHCnVZk8sXV991VhfE7Zj8_"
}
data = parse.urlencode(data).encode()
data1 = data.decode()
print(data)
print(type(data1))
print(data1)
def login():
    '''
    输入用户名和密码
    获取相应的登录cookie
    cookie写文件
    url1 = "http://date.jobbole.com/5659/"
    url_qq_login = "https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=208656&redirect_uri=http%3A%2F%2Fapi.blogqun.com%2Fauthorize.php&response_type=code&state=qzone3ff4daee80e0a4a682bad8e1ace7ca47%7CaHR0cDovL3d3dy5qb2Jib2xlLmNvbS9bd3Bd&scope=get_user_info%2Cadd_topic%2Cadd_one_blog%2Cupload_pic%2Cadd_share%2Cadd_t%2Cadd_pic_t%2Cget_info"
    :return:
    '''


    # 1. 找到登录入口
    #url_qq_login = "https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=208656&redirect_uri=http%3A%2F%2Fapi.blogqun.com%2Fauthorize.php&response_type=code&state=qzone3ff4daee80e0a4a682bad8e1ace7ca47%7CaHR0cDovL3d3dy5qb2Jib2xlLmNvbS9bd3Bd&scope=get_user_info%2Cadd_topic%2Cadd_one_blog%2Cupload_pic%2Cadd_share%2Cadd_t%2Cadd_pic_t%2Cget_info"




