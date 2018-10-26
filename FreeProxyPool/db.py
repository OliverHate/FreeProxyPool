# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 16:43
@Author     :邹文涛
@File       :db.py
@Software: PyCharm
"""
import redis
from FreeProxyPool.setting import REDIS_HOST,REDIS_PASSWD,REDIS_KEY,REDIS_PORT
from FreeProxyPool.setting import UNDECIDED_SCORCE,EFFECTIVE_SORCE,INVALID_SCORE
from FreeProxyPool.error import PoolEmptyError
from random import choice
import re
import logging
logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="FreeProxyPool/log/db_log.log",
                        filemode='a+')
class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWD):
        """
        初始化连接
        :param host: redis 地址
        :param port: redis 端口
        :param password: redis 密码
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=UNDECIDED_SCORCE):
        """
        添加代理，分数暂定
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """

        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+',proxy):
            # print('代理不符合规范',proxy,'丢弃')
            logging.error('代理不符合规范{}丢弃'.format(proxy))
            return
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        """
        随机获取有效代理

        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY,EFFECTIVE_SORCE,EFFECTIVE_SORCE)
        if len(result):
            return choice(result)
        else:
            raise PoolEmptyError
    def exists(self,proxy):
        """
        判断IP是否存在，
        :param proxy: 代理
        :return: 是否存在
        """

        return not self.db.zscore(REDIS_KEY,proxy) == None
    def effective(self,proxy):
        """
        检测代理可用，设置为可用
        :param proxy: 代理
        :return:
        """
        logging.info('代理{}设置为可用'.format(proxy))
        # print('代理{}设置为可用'.format(proxy))
        return self.db.zadd(REDIS_KEY,EFFECTIVE_SORCE,proxy)
    def invalid(self,proxy):
        logging.info('代理{}设置为不可用'.format(proxy))
        # print('代理{}设置为不可用'.format(proxy))
        return self.db.zadd(REDIS_KEY, INVALID_SCORE, proxy)
    def count(self):
        """
        获取代理池数量
        :return:
        """
        return self.db.zcount(REDIS_KEY,UNDECIDED_SCORCE,UNDECIDED_SCORCE)

    def all(self):
        """
        获取全部代理IP
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY,EFFECTIVE_SORCE,EFFECTIVE_SORCE)
    def batch(self,batch):
        return self.db.zrangebyscore(REDIS_KEY,UNDECIDED_SCORCE,UNDECIDED_SCORCE ,0,batch)

    def clear(self):
        return self.db.zremrangebyscore(REDIS_KEY,INVALID_SCORE,INVALID_SCORE)


if __name__ == '__main__':
    con = RedisClient()
    con.add('192.168.100.3:1')
    print(con.exists('192.168.100.1:1'))
    result = con.batch(10)
    print(result)