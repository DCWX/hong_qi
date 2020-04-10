# -*- utf-8 -*-
#@Time    :2019/9/1023:06
#@Author  :无邪
#@File    :test_case_data.py
#@Software:PyCharm
import unittest
from ddt import ddt,data
from common.read_excel import ReadExcel
from common.split_path import SplitPsth
from common.http_request import HttpRequest
from common.w_log import Mylog
from common.read_conf import ReadConf

@ddt#装饰测试类
class TestCaseData(unittest.TestCase):
    """单元测试"""
    case=ReadExcel(SplitPsth().split_case(), "Sheet1")
    cases=case.choice()
    # print(cases)
    def setUp(self):
        print("————————————————————————————————开始执行测试————————————————————————————————————")
    #装饰测试用例
    @data(*cases)
    def test_cases(self,testdata):
        res=HttpRequest().request_start(ReadConf(SplitPsth().split_conf()).read_request_methoid(),eval(testdata["Params"]),testdata["url"])
        # print(res)
        b = res["code"]  # 得到code的值
        c = res["msg"]  # 得到msg的值
        # print(b)
        # print(c)
        ecpected = testdata["ExpectedResult"]  # 得到预期结果
        ecpect = eval(ecpected)  # 转成原类型(字典)
        b1 = ecpect["code"]  # 得到code的值
        c1 = ecpect["msg"]  # 得到msg的值
        try:
            r = self.assertEqual(b, b1)  # 比较code
            r = self.assertEqual(c, c1)  # 比较msg
            print("正在执行用例【{}】：".format(testdata["Title"]))
            print("用例通过，实际结果{}与预期结果{}一致".format(res, eval(testdata["ExpectedResult"])))
            self.case.write_excel(testdata["Case_id"] + 1, 9, "PASS")
        except AssertionError as e:
            print("用例不通过，实际结果{}与预期结果{}不一致".format(res,eval(testdata["ExpectedResult"])))
            self.case.write_excel(testdata["Case_id"] + 1, 9, "FAILED")
            Mylog().log_debug(e)
            raise e
        finally:
           self.case.write_excel(testdata["Case_id"]+1,8,str(res))
    def tearDown(self):
        print("————————————————————————————————测试执行结束————————————————————————————————————")



if __name__ == '__main__':
        TestCaseData().test_cases()

