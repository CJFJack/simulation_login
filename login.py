# -*- encoding: utf-8 -*-
import requests


# 创建session对象，可以保存Cookie值
ssion = requests.session()

# 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 3需要登录的用户名和密码
data = {"username":"账户", "password":"密码"}

# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://cmdb.cy666.com/user_login/", data=data)

#  ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
r = ssion.post("http://cmdb.cy666.com/assets/data_cmdb_duty_schedule/")

# 打印响应内容
print (r.json())
