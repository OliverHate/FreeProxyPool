# -*- coding:utf-8 -*-
"""
@Time       :2018/10/26 8:57
@Author     :邹文涛
@File       :tester.py
@Software: PyCharm
"""
import asyncio
import aiohttp
import time
import sys
from math import  ceil
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from FreeProxyPool.db import RedisClient
from FreeProxyPool.setting import *
import logging
logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="FreeProxyPool/log/test_log.log",
                        filemode='a+')


class Tester(object):
    def __init__(self):
        self.db = RedisClient()

    async def test_single_proxy(self,proxy):
        """
        测试单个代理，设置为协程
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                async with session.get(TEST_URL,proxy=real_proxy,timeout=15,allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.db.effective(proxy)
                    else:
                        self.db.invalid(proxy)
                        logging.error('请求码不合法{}，IP{}'.format(*[response.status,proxy]))
                        # print('请求码不合法{}，IP{}'.format(*[response.status,proxy]))
            except Exception as e:
                print(e)
                self.db.invalid(proxy)
                logging.error("{}代理请求失败".format(proxy))
                # print("{}代理请求失败".format(proxy))
    def run(self):
        try:
            count = self.db.count()
            # print('当前剩余{}个代理未检测'.format(count))
            logging.info('当前剩余{}个代理未检测'.format(count))
            for i in range(ceil(count / BATCH_TEST_SIZE)):
                test_proxies = self.db.batch(BATCH_TEST_SIZE)
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            logging.critical('测试器发生错误{}'.format(e.args) )
            # print('测试器发生错误', e.args)

if __name__ == '__main__':
    s = Tester()
    s.run()