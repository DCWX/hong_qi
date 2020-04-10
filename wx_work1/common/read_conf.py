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
        self.conf=ConfigParser()
        self.conf.read(confname,encoding="utf-8")

    def read_choice(self):
        """用例选择方式"""
        btton=self.conf.get("choices","button")
        return btton

if __name__ == '__main__':
    r=ReadConf(SplitPsth().split_conf())
    print(r.read_choice())
