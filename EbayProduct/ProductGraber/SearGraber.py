# -*- coding:UTF-8 -*-

import sys
import time
import uuid
from urlparse import urlparse

from bs4 import BeautifulSoup

from DBImp.DBMysql import DBMysql
from ProductGraber.AGraber import AGraber

reload(sys)
sys.setdefaultencoding('utf-8')


class GrabSearsPhone(AGraber):
    def __init__(self, entrance_url, product_type, storage_table):
        AGraber.__init__(self)
        self.db = DBMysql()
        self.entrance_url = entrance_url
        self.product_type = product_type

        # self.searcher_xpath_value = searcher_xpath_value
        # self.searcher_submit_button = searcher_submit_button

        self.storage_table = storage_table
        pass

    def run(self):
        # 使用phantomjs虚拟浏览器
        driver = self.get_driver("chrome")
        self.handle_one_page(driver)

    def handle_one_page(self, driver):
        """重载父类方法，实现具体的爬虫操作"""

        url = self.entrance_url
        keyword = self.product_type
        driver.get(url)
        time.sleep(10)
        print "Inittial Page:",url
        # # driver = self.submit_initial_url(driver, "//input[@type='text']", "gh-btn", keyword) # ebay
        # #driver = self.submit_initial_url(driver, "//input[@type='search']", "search-button", keyword)
        #
        # driver.find_element_by_xpath("//*[@id='keyword']").clear()
        # driver.find_element_by_xpath("//*[@id='keyword']").send_keys(keyword)
        #
        # # 获取按钮对象并点击按钮
        # # elem = driver.find_element_by_id("search-button") # ebay ebuyer中使用该类型
        # # driver.find_element_by_xpath("//*[@id='goBtn']").click()
        # driver.find_element_by_id("goBtn").click()
        #
        # time.sleep(20)  # 需要暂停一两秒，防止页面未跳转
        # print "Get Crawer Home Page:", driver.current_url

        inputBoxXpath = "//*[@id='keyword']"

        driver.find_element_by_xpath(inputBoxXpath).clear()
        # elem = driver.find_element_by_id("keyword").send_keys(keyword)
        driver.find_element_by_xpath(inputBoxXpath).send_keys(keyword)
        # elem = driver.find_element_by_xpath(inputBoxXpath)
        # elem.clear()
        # elem = driver.find_element_by_xpath(inputBoxXpath)
        # elem.send_keys(keyword)

        # 获取按钮对象并点击按钮
        # searchButton = 'search-button'

        # elem = driver.find_element_by_css_selector('button.btn.btn-default')
        # elem = driver.find_element_by_css_selector('input.btn.btn-prim gh-spr')
        elem = driver.find_element_by_id("goBtn")
        #elem = driver.find_element_by_css_selector('# goBtn')
        # goBtn

        # elem = driver.find_element_by_xpath("//*[@id='goBtn']")
        elem.click()

        time.sleep(10)  # 需要暂停一两秒，防止页面未跳转
        print "Get Crawer Home Page:", driver.current_url

        i = 0
        while i < 21:
            # 获取当前网页html文档
            response_html = self.get_htmlcontent(driver.current_url)
            # if response_html is not None:
            try:
                if response_html.status_code is not 200:
                    print "Get status_code, but Exception:response_html.status_code=", response_html.status_code
                    break
            except:
                print "Exception:response_html.status_code=", response_html.status_code
                break

            # 仅提取内容部分的文档，方便解析提速
            # html_part_id_value =  "content"
            # # only_content_tags = SoupStrainer("ul", id=html_part_id_value)
            # only_content_tags = SoupStrainer("div", id=html_part_id_value)
            # html_part_content = BeautifulSoup(response_html.text, "html.parser", parse_only=only_content_tags).prettify()
            #
            # # 解析所需的所有链接
            # soup = BeautifulSoup(html_part_content, "html.parser", from_encoding="utf-8")
            # # links = soup.find_all('a', href=re.compile("phone", re.I))


            soup = BeautifulSoup(response_html.text, "html.parser", from_encoding="utf-8")
            #links = soup.find_all('a', href=re.compile(r"phone", re.I))
            links = soup.find_all('a')
            for link in links:
                url_parse = urlparse(url)
                domain = url_parse.scheme + "://" + url_parse.netloc
                new_url = domain + link['href']
                self.handle_result_url(new_url, keyword, i)
                print "Fetch a phone url :", new_url
                time.sleep(10)

            i = i+1

            # current_page = "a.pg  curr"
            # print "The ", driver.find_element_by_css_selector(current_page).text, " Has Finished"

            try:
                # nextPage = "a.gspr.next"
                # driver.find_element_by_css_selector(nextPage).click()　#ebay

                # 获取下一页的链接
                driver.find_element_by_xpath("//*[@id='pagination']/div[1]/div[2]/a/span").click()
            except:
                break
            print driver.current_url
            time.sleep(20)

        driver.quit()
        self.db.close()

    # 加个关键词，传入type
    def handle_result_url(self, item_url, keyword, i):
        print "Handle", i, "Page's URL:", item_url

        response_html = self.get_htmlcontent(item_url)
        # if response_html is not None:
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