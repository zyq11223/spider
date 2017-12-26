# -*- coding:UTF-8 -*-

import logging
import re
import sys
import time
import uuid
from urlparse import urlparse

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from DBImp.DBMysql import DBMysql
from ProductGraber.AEbayGraber import AEbayGraber

reload(sys)
sys.setdefaultencoding('utf-8')


class ProductDBObejct:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.domain = ""
        self.keyword = ""
        self.url = ""
        self.title = ""
        self.doc = ""


class EbayGraber(AEbayGraber):
    def __init__(self, entrance_url, product_type, storage_table):
        AEbayGraber.__init__(self)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(module)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y %b %d %H:%M:%S',
                            filename='./app.Log',
                            filemode='w')
        self.db = DBMysql()
        self.entrance_url = entrance_url
        self.product_type = product_type
        self.storage_table = storage_table
        pass

    def get_soup_responser(self, html_text_content, html_psrser = "html.parser", from_encoding = "utf-8"):
        """根据网页内容，构建soup对象，并返回"""
        return BeautifulSoup(html_text_content, html_psrser, from_encoding=from_encoding)

    def get_strainer_soup_responser(self, html_text_content, strainer_symbol, html_psrser = "html.parser", from_encoding = "utf-8"):
        """根据由SoupStrainer限定的部分网页内容，构建soup对象，并返回"""
        only_content_tags = SoupStrainer(id=strainer_symbol)    # todo：修改soupStrainer为多种构造方式自选，使用枚举类型、传入参数、switch确定
        only_content = BeautifulSoup(html_text_content, html_psrser,  parse_only= only_content_tags).prettify()
        return BeautifulSoup(only_content, html_psrser, from_encoding=from_encoding)

    def web_page_paser(self, driver):
        """解析所有有效的网页内容"""
        keyword = self.product_type

        driver.get(self.entrance_url)
        time.sleep(10)

        print "Inittial Page:",self.entrance_url

        driver = self.submit_initial_url(driver, "//input[@type='text']", "gh-btn", keyword)

        i = 0
        while i < 500:
            request_responser = self.get_request_responser(driver.current_url)
            if request_responser is None:
                break

            soup = self.get_strainer_soup_responser(request_responser.text, "CenterPanel")
            links = soup.find_all('a', href = re.compile(keyword))
            print links
            for link in links:
                new_url = link['href']
                self.handle_one_url(new_url, keyword, i)
                time.sleep(10)

            i = i+1

            # current_page = "a.pg  curr"
            # print "The ", driver.find_element_by_css_selector(current_page).text, " Has Finished"

            try:
                driver.find_element_by_css_selector("a.gspr.next").click()
                print "Geting a new page,url=%s", driver.current_url
                time.sleep(20)
            except:
                print "Error:Geting next page Failed", request_responser.status_code
                break

        driver.quit()
        self.db.close()

    # 加个关键词，传入type
    def handle_one_url(self, url, keyword, i):
        logging.info("Handle the" + str(i)+ "th URL" + url)

        response_html = self.get_request_responser(url)
        try:
            if response_html.status_code is not 200:
                pass
        except:
            print "LOG:Exception:EbayGraber %s handle_one_url response_html.status_code=%s! url=%s", self.product_type, response_html.status_code, url
            pass

        if response_html.text is not None:
            new_reconrd =  self.get_db_product_db_object(url, response_html.text)
            if new_reconrd is not None:
                self.db.insertOneData(self.storage_table, new_reconrd)
        else:
            print "LOG:Warning:EbayGraber %s handle_one_url response_html.text is None! url=%s" % self.product_type, url


    def get_db_product_db_object(self, url, response_html_text):
        """解析抽取到的商品链接，判断是否是所需处理的网页，返回一个可以入库的字典"""
        soup = BeautifulSoup(response_html_text, "html.parser")
        try:
            item_title = ""
            if soup.title is not None:
                if self.product_type not in soup.title.string or "camera | eBay" in soup.title.string:
                    logging.warn("This is not a " + self.product_type + " product url! url=" + url)
                    return None
                item_title = soup.title.string.replace('\"', ' ')

            item_content = ""
            if response_html_text is not None:
                item_content = response_html_text.replace('\"', ' ')

            new_record = {"id": str(uuid.uuid4()),
                           "domain_name": urlparse(url).scheme + "://www." + urlparse(url).netloc,
                           "keyword": self.product_type,
                           "url": url,
                           "title": item_title,
                           "doc": self.db.escape_string(unicode(item_content))
                           }
            return new_record
        except:
            pass

