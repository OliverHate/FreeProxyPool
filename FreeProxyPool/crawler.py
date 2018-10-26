# -*- coding:utf-8 -*-
"""
@Time       :2018/10/25 14:21
@Author     :邹文涛
@File       :crawler.py
@Software: PyCharm
"""
import re
import logging
from time import sleep
from FreeProxyPool.utils import get_source_code
logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
                        filename="FreeProxyPool/log/get_log.log",
                        filemode='a+')
class ProxyMetaClass(type):

    def __new__(cls, name,bases,attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'Crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=ProxyMetaClass):

    def get_proxyies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            # print('成功抓取代理',proxy)
            logging.info("成功抓取IP {}".format(proxy))
            proxies.append(proxy)
        return proxies

    def crawl_xroxy(self):
        for i in ['CN', 'TW']:
            start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(i)
            html = get_source_code(start_url)
            if html:
                ip_address1 = re.compile("title='View this Proxy details'>\s*(.*).*")
                re_ip_address1 = ip_address1.findall(html)
                ip_address2 = re.compile("title='Select proxies with port number .*'>(.*)</a>")
                re_ip_address2 = ip_address2.findall(html)
                for address, port in zip(re_ip_address1, re_ip_address2):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')

    def Crawl_data5u(self):
        start_url = 'http://www.data5u.com/free/gngn/index.shtml'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=47AA0C887112A2D83EE040405F837A86',
            'Host': 'www.data5u.com',
            'Referer': 'http://www.data5u.com/free/index.shtml',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        }
        html = get_source_code(start_url, options=headers)
        if html:
            ip_address = re.compile('<span><li>(\d+\.\d+\.\d+\.\d+)</li>.*?<li class=\"port.*?>(\d+)</li>', re.S)
            re_ip_address = ip_address.findall(html)
            for address, port in re_ip_address:
                result = address + ':' + port
                yield result.replace(' ', '')







    def Crawl_iphai(self):
        start_url = 'http://www.iphai.com/'
        html = get_source_code(start_url)
        if html:
            find_tr = re.compile('<tr>(.*?)</tr>', re.S)
            trs = find_tr.findall(html)
            for s in range(1, len(trs)):
                find_ip = re.compile('<td>\s+(\d+\.\d+\.\d+\.\d+)\s+</td>', re.S)
                re_ip_address = find_ip.findall(trs[s])
                find_port = re.compile('<td>\s+(\d+)\s+</td>', re.S)
                re_port = find_port.findall(trs[s])
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')






    def Crawl_ip3366(self):
        for i in range(1, 4):
            sleep(2)
            start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
            html = get_source_code(start_url)
            if html:
                find_tr = re.compile('<tr>(.*?)</tr>', re.S)
                trs = find_tr.findall(html)
                for s in range(1, len(trs)):
                    find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                    re_ip_address = find_ip.findall(trs[s])
                    find_port = re.compile('<td>(\d+)</td>')
                    re_port = find_port.findall(trs[s])
                    for address, port in zip(re_ip_address, re_port):
                        address_port = address + ':' + port
                        yield address_port.replace(' ', '')

    def Crawl_xicidaili(self):
        for i in range(2,5):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFmOWIxZGE0MDNlYzAxNmJmYWY3ZWMxM2ZkMTQyOTA5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTE2TjBHNm1zWXFQTFRyenJJYXZkckg4RGhIV2tSVklPWTFiQ01iZ2xrWnc9BjsARg%3D%3D--ba4943e0dbdaadef63f6855817aef42fa109714b; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1540450411; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1540450687',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests': '1',
            }
        soucrce_code = get_source_code(start_url,options=headers)
        if soucrce_code:
            find_trs = re.compile('<tr class.*?>(.*?)</tr>',re.S)
            trs = find_trs.findall(soucrce_code)
            for tr in trs:
                find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                re_ip_address = find_ip.findall(tr)
                find_port = re.compile('<td>(\d+)</td>')
                re_port = find_port.findall(tr)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')

    def Crawl_kuaidaili(self):
        for i in range(1, 6):
            sleep(1)
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_source_code(start_url)
            if html:
                ip_address = re.compile('<td data-title="IP">(.*?)</td>')
                re_ip_address = ip_address.findall(html)
                port = re.compile('<td data-title="PORT">(.*?)</td>')
                re_port = port.findall(html)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')

