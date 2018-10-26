# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 16:43
@Author     :邹文涛
@File       :error.py
@Software: PyCharm
"""
class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')
    def __repr__(self):
        return repr('代理池已经枯竭')