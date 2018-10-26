# -*- coding:utf-8 -*-
"""
@Time       :2018/10/26 10:36
@Author     :邹文涛
@File       :api.py
@Software: PyCharm
"""
from flask import Flask, g,render_template

from FreeProxyPool.db import RedisClient


__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/getIP')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/api/v1/IPcount')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.all())


if __name__ == '__main__':
    app.run('127.0.0.1',5555)
