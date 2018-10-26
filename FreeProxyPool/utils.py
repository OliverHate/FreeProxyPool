# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 14:46
@Author     :邹文涛
@File       :utils.py
@Software: PyCharm
"""
import requests
import  random
import logging
from requests.exceptions import ConnectionError
logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="FreeProxyPool/log/requests_log.log",
                        filemode='a+')
# 浏览器表头
headers_all = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)"},
    {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0"}
]
base_headers = {"User-Agent": random.choice(headers_all)["User-Agent"],
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
           }

def get_source_code(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers, **options)
    # print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        # print('抓取成功', url, response.status_code)
        logging.info('{}访问失败,状态码:{}'.format(*[url,response.status_code]))
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        logging.warning('{}访问失败'.format(url))
        # print('抓取失败', url)
        return None