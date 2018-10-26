# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 16:46
@Author     :邹文涛
@File       :setting.py
@Software: PyCharm
"""

# REDIS数据库地址
REDIS_HOST = '127.0.0.1'

#REDIS 密码 如无写None
REDIS_PASSWD = None
#数据库端口
REDIS_PORT = 6379
REDIS_KEY ='proxy'
#代理分数
EFFECTIVE_SORCE = 1
UNDECIDED_SCORCE=0
INVALID_SCORE = -1

#网页成功状态码
VALID_STATUS_CODES = [200,302]
#代理池数量界限
POOL_UPPER_THRESHOLD = 50000
#检查周期
TESTER_CYCLE = 200
#获取周期
GETTER_CYCLE = 600
#清洗周期
CLEAR_CYCLE = 3600
#测试URL，
TEST_URL="https://www.lagou.com/"

#API配置
API_HOST='0.0.0.0'
API_PORT=5000

#开关
TESTER_ENABLED = True
GETTER_ENABLED =True
CLEAR_ENABLED =True
API_ENABLED = True

#最大批测试量
BATCH_TEST_SIZE = 20