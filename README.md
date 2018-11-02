# FreeProxyPool
2018.11.2  
该IP池使用redis和python3搭建， 具体实现逻辑为，爬取各个代理网站的免费IP，进行对目标网站的检测，如果IP可用，则由flask调用，如果不可用，可定时清洗不可用IP。  
缺陷：目前未编写IP池过时时间，未编写可用IP过期方法。

## 环境：
linux和windows均可（实测win10和centos7）  
windows:python3.6  
linux:python3.7 （python3.5以上均可）  
redis （测试环境为redis3.2）   

## 下载链接
redis
> windows: https://github.com/MicrosoftArchive/redis/releases  
linux: http://download.redis.io/releases/redis-4.0.11.tar.gz

## 安装依赖
win and linux:
> pip3 install -r requirements.txt

## 运行
> python3 run.py  

## 获取代理

利用requests获取代理

```python
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5000/api/v1/getIP'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```
可直接访问 `http://IP:port` 查看图文教程

## 调试
具体配置参数在 `setting.py`文件内
```python
# REDIS数据库地址
REDIS_HOST = '127.0.0.1'

#REDIS 密码 如无写None
REDIS_PASSWD = None
#数据库端口
REDIS_PORT = 6379
#数据库键值
REDIS_KEY ='proxy'
#代理分数
# 可用
EFFECTIVE_SORCE = 1
# 待检测
UNDECIDED_SCORCE=0
# 不可用
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
# aip端口
API_PORT=5000

#开关
# 定时测试开关
TESTER_ENABLED = True
# 定时获取开关
GETTER_ENABLED =True
# 定时清洗开关
CLEAR_ENABLED =True
# 开启API开关
API_ENABLED = True

#最大批测试量
BATCH_TEST_SIZE = 20
```

## 项目参考：
https://github.com/WiseDoge/ProxyPool
