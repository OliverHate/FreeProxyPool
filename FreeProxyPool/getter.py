# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 14:31
@Author     :邹文涛
@File       :getter.py
@Software: PyCharm
"""
import sys
import logging
from FreeProxyPool.crawler import Crawler
from FreeProxyPool.db import RedisClient
from FreeProxyPool.setting import POOL_UPPER_THRESHOLD


logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="FreeProxyPool/log/get_log.log",
                        filemode='a+')
class Getter():
    def __init__(self):
        self.crawler = Crawler()
        self.redis = RedisClient()
    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        :return:
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        # print('爬取代理开始')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxyies(callback)
                sys.stdout.flush() #LINUX有区别，单秒输出字符
                for proxy in proxies:
                    if not self.redis.exists(proxy):
                        self.redis.add(proxy)
                    else:
                        # print("{}已经存在在IP池".format(proxy))
                        logging.info("重复抓取IP {}".format(proxy))
if __name__ == '__main__':
    s = Getter()
    s.run()