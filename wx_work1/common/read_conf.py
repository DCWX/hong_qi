# -*- utf-8 -*-
#@Time    :2019/9/422:37
#@Author  :无邪
#@File    :read_conf.py
#@Software:PyCharm

from configparser import ConfigParser
from common.split_path import SplitPsth
class ReadConf:
    """读取配置文件的类"""
    def __init__(self,confname):
        self.conf=ConfigParser()#创建对象
        self.conf.read(confname,encoding="utf-8")#打开配置文件

    def read_choice(self):
        """用例选择方式"""
        btton=self.conf.get("choices","button")
        return btton

    def read_request_methoid(self):
        """读取请求方法"""
        request_method=self.conf.get("torequest","to_request")
        return request_method

if __name__ == '__main__':
    r=ReadConf(SplitPsth().split_conf())
    print(r.read_choice())
    print(r.read_request_methoid())
