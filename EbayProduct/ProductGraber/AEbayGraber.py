# -*- coding:UTF-8 -*-

import os
import time
import random
import requests
import threading
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class AEbayGraber(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.user_agents = list()
        self.load_user_agents()
        pass

    def run(self):
        driver = self.get_driver("phantomjs")
        self.web_page_paser(driver)

    def web_page_paser(self, driver):
        """具体处理网页的方法交给继承者实现"""
        pass

    def get_driver(self, driver_name):
        if driver_name == "chrome":
            driver_path = "D:\App\Google\Chrome\Application\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driver_path
            driver = webdriver.Chrome(driver_path)
        elif driver_name == "phantomjs":
            driver = webdriver.PhantomJS(executable_path="C:\Program Files\Python27\Scripts\phantomjs.exe")
        return driver

    def load_user_agents(self):
        """load user agenet from file"""
        fp = open('.\config\user_agents', 'r')
        line = fp.readline().strip('\n')
        while(line):
            self.user_agents.append(line)
            line = fp.readline().strip('\n')
        fp.close()

    def submit_initial_url(self, driver, search_xpath_value, submit_key, keyword):

        # 输入搜索词
        driver.find_element_by_xpath(search_xpath_value).clear()
        driver.find_element_by_xpath(search_xpath_value).send_keys(keyword)

        # 获取按钮对象并点击按钮
        elem = driver.find_element_by_id(submit_key)
        elem.click()

        time.sleep(20)   # 需要暂停一两秒，防止页面未跳转
        print "Get Crawer Home Page:", driver.current_url
        return driver

    def get_request_responser(self, url):
        """get html content by requests method"""
        length = len(self.user_agents)
        index = random.randint(0, length-1)
        user_agent = self.user_agents[index]

        headers = {}
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers['Accept-Encoding'] = 'gzip, deflate, sdch'
        headers['Accept-Language'] = 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
        headers['Connection'] = 'keep-alive'
        headers['User-Agent'] = user_agent

        try:
            #cookies = "" # 制空了还有啥用
            #cookies = requests.get(url, headers=headers).cookies
            #request_responser = requests.get(url, user_agent, verify=False, cookies=cookies)
            request_responser = requests.get(url, user_agent, verify=False)
            if request_responser.status_code is 200:
                return request_responser
            else:
                print "Error:Getting request responser Failed! url=%s,user_agent=%s" % url, user_agent
                return None

        except:
            print "Error:Getting request responser Failed! url=%s,user_agent=%s" % url, user_agent




#
# my_headers = [
#                     "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
#                     "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
#                     "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
#                     "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
#                     ]
#         random_header = random.choice(my_headers)
#
# headers_base = {
#                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                     'Accept-Encoding': 'gzip, deflate, sdch',
#                     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
#                     'Connection': 'keep-alive',
#                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
#                     }