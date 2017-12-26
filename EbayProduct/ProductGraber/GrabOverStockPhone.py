# -*- coding:UTF-8 -*-

import re
import sys
import time
import uuid
from urlparse import urlparse

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from DBImp.DBMysql import DBMysql
from ProductGraber.AGraber import AGraber

reload(sys)
sys.setdefaultencoding('utf-8')


class GrabOverStockPhone(AGraber):
    def __init__(self, entrance_url, product_type, storage_table):
        AGraber.__init__(self)
        self.db = DBMysql()
        self.entrance_url = entrance_url
        self.product_type = product_type

        # self.searcher_xpath_value = searcher_xpath_value
        # self.searcher_submit_button = searcher_submit_button

        self.storage_table = storage_table
        pass

    def handle_one_page(self, driver):
        """重载父类方法，实现具体的爬虫操作"""

        url = self.entrance_url
        keyword = self.product_type
        driver.get(url)

        time.sleep(120)
        try:
            driver.find_element_by_id("cboxClose").click()
            print "Click the pop - up windows"
        except:
            pass
        time.sleep(60)

        print "Inittial Page:",url
        # driver = self.submit_initial_url(driver, "//input[@type='text']", "gh-btn", keyword) # ebay
        #driver = self.submit_initial_url(driver, "//input[@type='search']", "search-button", keyword)

        driver.find_element_by_xpath("//*[@id='search-input']").clear()
        driver.find_element_by_xpath("//*[@id='search-input']").send_keys(keyword)

        # 获取按钮对象并点击按钮
        # elem = driver.find_element_by_id(submit_key) # ebay ebuyer中使用该类型
        elem = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset[2]/label/i')
        elem.click()

        time.sleep(60)
        # 翻页的一种变种，将页面滚动条拖到底部
        i = 0
        while i < 200:      ###################################################################################   2000
            js = "var q=document.body.scrollTop=" + str(10000 * i)
            print i, js
            driver.execute_script(js)
            time.sleep(3)
            i = i + 1

        # 获取当前网页html文档
        print "Get Crawer Home Page:", driver.current_url
        response_html = self.get_htmlcontent(driver.current_url)
        try:
            if response_html.status_code is not 200:
                print "Get status_code, but Exception:response_html.status_code=", response_html.status_code
                pass
        except:
            print "Exception:response_html.status_code=", response_html.status_code
            pass

        # 仅提取内容部分的文档，方便解析提速
        html_part_id_value =  "result-products"
        only_content_tags = SoupStrainer(id=html_part_id_value)
        html_part_content = BeautifulSoup(response_html.text, "html.parser", parse_only=only_content_tags).prettify()

        # 解析所需的所有链接
        soup = BeautifulSoup(html_part_content, "html.parser", from_encoding="utf-8")
        # links = soup.find_all('a', class_='jsQs', href=re.compile(self.product_type, re.I))

        if keyword is "cellphone":
            url_judger = "phone"
        elif keyword is "tv":
            url_judger = "tv"
        elif keyword is "digit camera":
            url_judger = "camera"
        elif keyword is "bike":
            url_judger = "bike"
        elif keyword is "labtop":
            url_judger = "labtop"
        elif keyword is "mice":
            url_judger  = "mice"
        elif keyword is "Webcams":
            url_judger  = "Webcams"
        elif keyword is "shaver":
            url_judger  = "shaver"
        elif keyword is "flashlight":
            url_judger  = "flashlight"
        elif keyword is "watch":
            url_judger = "watch"

        links = soup.find_all('a', href=re.compile(url_judger, re.I))      # 注意，这里的phone，不一定等于keyword了！！！！！！！！！！！！！！！！！！！！！
        print len(links)
        for link in links:
            new_url = link['href']
            self.handle_result_url(new_url, keyword, i)
            time.sleep(10)

            # current_page = "a.pg  curr"
            # print "The ", driver.find_element_by_css_selector(current_page).text, " Has Finished"

            # try:
            #     # nextPage = "a.gspr.next"
            #     #　driver.find_element_by_css_selector(nextPage).click()　#ebay
            #
            #     # driver.find_element_by_xpath("//*[@id='main-content']/div/div[1]/div[2]/div[1]/ul/li[6]/a").click()  # Cdicount
            #
            #     nextPage = "a.jsNxtPage.pgNext"
            #     driver.find_element_by_css_selector(nextPage).click()
            # except:
            #     break
            # print driver.current_url
            time.sleep(20)

        driver.quit()
        self.db.close()

    # 加个关键词，传入type
    def handle_result_url(self, item_url, keyword, i):
        print "Handle", i, "Page's URL:", item_url

        response_html = self.get_htmlcontent(item_url)
        if response_html.status_code == 200:
            try:
                item_domain = urlparse(item_url).scheme + "://www." + urlparse(item_url).netloc
                item_content = response_html.text.replace('\"', ' ')
                html_content = BeautifulSoup(response_html.text, "html.parser")
                item_title = html_content.title.string.replace('\"', ' ')
                new_reconrd = {"id":str(uuid.uuid4()),
                               "domain_name":item_domain,
                               "keyword":keyword,
                               "url":item_url,
                               "title":item_title,
                               "doc":self.db.escape_string(unicode(item_content))
                               }
                if "| eBay" is not item_title :
                    self.db.insertOneData(self.storage_table, new_reconrd)
            except:
                pass
        else:
            print "Handle", i, "Page's URL:", item_url, "Failed!..............................................."