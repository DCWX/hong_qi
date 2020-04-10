# -*- utf-8 -*-
#@Time    :2019/9/422:38
#@Author  :无邪
#@File    :http_request.py
#@Software:PyCharm
import requests
class HttpRequest:
    """http请求类"""
    def request_start(self,method,params,url):
        """设置请求"""
        if str(method).upper() == "GET":
           res=requests.get(url=url,params=params)
           return res.json()
        elif str(method).upper() == "POST":
            res=requests.post(url=url,data=params)
            return res.json()
        else:
            print("程序异常，请检查请求数据")
if __name__ == '__main__':
    r=HttpRequest()
    res=r.request_start("get",{"mobilephone":"18258148330","pwd":"wx123456"},"http://test.lemonban.com/futureloan/mvc/api/member/login")
    print(res)
