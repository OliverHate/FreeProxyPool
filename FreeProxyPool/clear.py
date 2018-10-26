# -*- coding:utf-8 -*-
"""
@Time       :2018/10/26 16:50
@Author     :邹文涛
@File       :clear.py
@Software: PyCharm
"""

from FreeProxyPool.db import RedisClient
import logging
logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="./log/clear_log.log",
                        filemode='a+')
class clear():
    def __init__(self):
        self.db = RedisClient()
    def run(self):
        num = self.db.clear()
        logging.info("清除{}个无效IP".format(num))

if __name__ == '__main__':
    s = clear()
    print(s.run())