# -*- utf-8 -*-
#@Time    :2019/9/110:04
#@Author  :无邪
#@File    :run.py
#@Software:PyCharm
import unittest
from common import test_case_data
import HTMLTestRunnerNew
from common.split_path import SplitPsth
class TestsuitRun:
    """测试集"""
    def test_suit(self):
        suit=unittest.TestSuite()#创建测试集
        load=unittest.TestLoader()#创建加载器
        suit.addTest(load.loadTestsFromModule(test_case_data))

        with open(SplitPsth().split_report(),"wb") as file:
            r=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                             verbosity=2,
                                             title="红旗接口测试报告",
                                             description="第一次运行",
                                             tester="无邪")
            r.run(suit)
if __name__ == '__main__':
    TestsuitRun().test_suit()