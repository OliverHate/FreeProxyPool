# -*- coding:utf-8 -*-
"""
@Time       :2018/10/26 16:36
@Author     :邹文涛
@File       :scheduler.py
@Software: PyCharm
"""

from time import sleep
from multiprocessing import Process
from FreeProxyPool.api import app
from FreeProxyPool.getter import Getter
from FreeProxyPool.tester import Tester
from FreeProxyPool.setting import *
from FreeProxyPool.clear import clear

class Scheduler(object):
    def schedule_tester(self,cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            tester.run()
            sleep(cycle)
    def schedule_getter(self,cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter  = Getter()
        while True:
            getter.run()
            sleep(cycle)
    def schedule_clear(self,cycle=CLEAR_CYCLE):
        cls = clear()
        while True:
            cls.run()
            sleep(cycle)

    def schedule_api(self):
        """
        开启API
        :return:
        """
        app.run(host=API_HOST, port=API_PORT)


    def run(self):
        print('IP池启动')


        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
        if CLEAR_ENABLED:
            cls_process = Process(target=self.schedule_clear)
            cls_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
if __name__ == '__main__':
    s = Scheduler()
    s.run()