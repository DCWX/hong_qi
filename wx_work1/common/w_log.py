# -*- utf-8 -*-
#@Time    :2019/9/422:40
#@Author  :无邪
#@File    :w_log.py
#@Software:PyCharm
import logging
from common.split_path import SplitPsth
class Mylog:
    "日志类"
    def  mylog(self,level,Msg):
        mylog=logging.getLogger("mylog")#创建日志收集器
        mylog.setLevel(level)#设置日志收集级别

        console=logging.StreamHandler()#输出到控制台
        console.setLevel(level)#设置输出级别
        simple_format =logging.Formatter('[%(name)s]-[%(asctime)s]-[%(filename)s:%(lineno)d]-[%(levelname)s]-[%(message)s]')
        console.setFormatter(simple_format)#设置日志输出格式

        fc=logging.FileHandler(SplitPsth().split_log(),encoding="utf-8")#输出到指定文件
        fc.setLevel(level)
        fc.setFormatter(simple_format)

        mylog.addHandler(console)#添加输出渠道
        mylog.addHandler(fc)#添加输出渠道
        if level=="DEBUG":
            mylog.debug(Msg)
        elif level=="INFO":
            mylog.info(Msg)
        elif level=="WARRING":
            mylog.warning(Msg)
        elif level=="ERROR":
            mylog.error(Msg)
        else:
            mylog.critical(Msg)
        #移除日志输出渠道
        mylog.removeHandler(fc)
        mylog.removeHandler(console)

    def log_debug(self,Msg):
        """收集debug级别日志"""
        self.mylog("DEBUG",Msg)
    def log_info(self,Msg):
        self.mylog("INFO", Msg)

    def log_warring(self, Msg):
        self.mylog("WARRING", Msg)

    def log_error(self, Msg):
        self.mylog("ERROR", Msg)

    def log_critical(self, Msg):
        self.mylog("CRITICAL", Msg)

if __name__ == '__main__':
    Mylog().log_debug("这是一条debug消息")
    Mylog().log_critical("这是一个严重的bug")