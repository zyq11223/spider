# -*- coding:UTF-8 -*-
import re
import time
import random
import urllib2
import threading
import requests
from bs4 import BeautifulSoup


class IPProxyPool(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pool = []

    def run(self):
        self.get_ip_proxies()

    def get_proxies(self):
        """获取IP代理池数据"""
        if len(self.pool) == 0:
            return None
        else:
            return self.pool

    def get_ip_proxies(self):
        """获取所有的ip代理池"""
        url_list = list()
        start_url = "http://www.xicidaili.com/nt/"
        url_list.append(start_url)
        for i in range(2, 100):
            aim_url = start_url + "/" + str(i)
            url_list.append(aim_url)

        headers_base = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }
        _cookies = ""

        for u in url_list:
            _cookies = requests.get("http://www.xicidaili.com/", headers=headers_base).cookies
            r = requests.get(u , headers=headers_base, cookies=_cookies)
            html_doc = r.text

            if r.status_code is not 200:
                continue

            groupData = []
            soup = BeautifulSoup(html_doc)
            group = soup.find_all("tr", class_="odd")
            for onedata in group:
                temp = []
                ip = (onedata.find_all("td"))[1].string
                port = (onedata.find_all("td"))[2].string
                # print "IP:%s\tPort:%s" % (ip, port)
                groupData.append([ip, port])

            r.close()

            # 验证ip可用性
            print '找到当前%s的共有%d个ip' % (u, len(groupData))
            count = 0
            for key, value in groupData:
                # print key,value
                proxy_handler = urllib2.ProxyHandler({"http": '%s:%s' % (key, value)})
                opener = urllib2.build_opener(proxy_handler)
                urllib2.install_opener(opener)

                try:
                    request = urllib2.Request("http://ip.chinaz.com/getip.aspx")
                    response = urllib2.urlopen(request, timeout=5)
                    ip = key
                    port = value
                    http_ip = "http://" + '%s:%s' % (key, value)
                    proxy = dict(http=http_ip)
                    self.pool.append(proxy)
                    continue
                except Exception:
                    print "(+) Wrong ip-------"
                    continue
            time.sleep(60)

if __name__ == '__main__':
    poll  = IPProxyPool()
    poll.get_ip_proxies()