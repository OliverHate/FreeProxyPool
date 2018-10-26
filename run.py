# -*- coding:utf-8 -*-
"""
@Time       :2018/10/26 17:24
@Author     :邹文涛
@File       :run.py
@Software: PyCharm
"""
from FreeProxyPool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()
if __name__ == '__main__':
    main()