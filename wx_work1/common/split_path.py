# -*- utf-8 -*-
#@Time    :2019/9/422:37
#@Author  :无邪
#@File    :split_path.py
#@Software:PyCharm
import os

class SplitPsth:
    """文件路径"""
    def __init__(self):
        # self.b=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#方法一
        self.d=os.path.split(os.path.dirname(__file__))[0]#方法二
        #注意：不能使用os.getcwd()报错

    def split_case(self):
        """拼接用例路径"""
        test_case_dir=os.path.join(self.d,"test_case","红旗接口测试用例.xlsx")
        return test_case_dir
    def split_conf(self):
        """拼接配置文件路径"""
        test_conf_dir=os.path.join(self.d,"conf","use.conf")
        return test_conf_dir
    def split_log(self):
        '''日志路径拼接'''
        test_log_dir=os.path.join(self.d,"test_result","wx.log")
        return test_log_dir
    def split_report(self):
        ''' 测试报告路径'''
        test_report=os.path.join(self.d,"test_result","wx.html")
        return test_report
if __name__ == '__main__':
    path=SplitPsth()
    # print(path.split_case())
    # print(path.split_conf())
