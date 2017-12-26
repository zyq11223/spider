#-*- coding:UTF-8 -*-
import os
import random
import re
import sys
import time
import uuid
from urlparse import urlparse

import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver

from DBImp.DBMysql import DBMysql

reload(sys)
sys.setdefaultencoding('utf-8')

# 加个关键词，传入type
def handle_result_url(url, i):
    # 或者调用另一个类的对象，将其放到另一个对象中，对其进行处理，存库
    # 请求一下该网页，然后，获取title，获取url，保存文档文件，根据url筛选出网络域名：https://segmentfault.com/q/1010000002570649
    # 保存到存放到数据库线程中，保存到数据库

    # 获取当前网页html文档
        my_headers = [
                    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
                    "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
                    ]

        # try:
        random_header = random.choice(my_headers)
        response_html = requests.get(url,random_header,verify=False)

        if response_html.status_code == 200:
            fileParser = "html.parser"
            html_content = BeautifulSoup(response_html.text, fileParser)#以及编码值
            print html_content.title
            print "handle_selected_url", url, i

            url_parse = urlparse(url)
            domain = url_parse.scheme + "://www." + url_parse.netloc
            keyword = "bike"
            # record = "INSERT INTO 0spider.online_product_news_data(id, domain_name, keyword, url, title, doc)VALUES ( " + str(uuid.uuid4()) + ", " + domain + ", " + keyword +", "+ url +", " + html_content.title  +", " + response_html.text + ")"

            url_parse = urlparse(url)
            domain = url_parse.scheme + "://www." + url_parse.netloc
            keyword = "bike"

            #构造用来插入数据的字典
            new_reconrd = {"id":str(uuid.uuid4()),
                           "domain_name":domain,
                           "keyword":keyword,
                           "url":url,
                           "title":str(html_content.title.string),
                           "doc":db.escape_string(unicode(response_html.text))
                        }


            # record = "INSERT INTO 0spider.online_product_news_data(id, domain_name, keyword, url, title, doc)VALUES ( " + "\"" + str(uuid.uuid4()) + "\"" + ", " + "\"" + domain + "\"" + ", " + "\"" + keyword +"\"" + ", "+ "\"" + url +"\"" + ", " + "\"" + str(html_content.title) + "\"" +", " + "\"" + db.escape_string(unicode(response_html.text)) +  "\"" + ")" 

            db.insertOneData("online_retail_products_data_google_phone",new_reconrd)
            #db.dml(record)
            print new_reconrd
            print "a a a  a a a a a a aa a   data"


def GetPage(driver,keyword, url):
    
    driver.get(url)

    #　获取Yahoo输入框对象，并提交关键词
    #inputBoxXpath = "//input[@name='kwd']"

    inputBoxXpath = "//*[@id='keyword']"

    driver.find_element_by_xpath(inputBoxXpath).clear()
    driver.find_element_by_xpath(inputBoxXpath).send_keys(keyword)
    # elem = driver.find_element_by_xpath(inputBoxXpath)
    # elem.clear()
    # elem = driver.find_element_by_xpath(inputBoxXpath)
    # elem.send_keys(keyword)
    
    # 获取按钮对象并点击按钮
    searchButton = 'search-button'
    
    # elem = driver.find_element_by_css_selector('button.btn.btn-default')
    # elem = driver.find_element_by_css_selector('input.btn.btn-prim gh-spr')
    # elem = driver.find_element_by_id("gh-btn")

    elem = driver.find_element_by_xpath("//*[@id='goBtn']")
    elem.click()
    print "Home Page         :", driver.current_url

    # 需要暂停一两秒，防止页面未跳转，后续拿出了链接
    time.sleep(5)

    print "Search Engines    :", driver.current_url
    print "Currenturl title  :",driver.title

    i = 0

    while i < 5:
        # 获取当前网页html文档
        my_headers = [
                    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
                    "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
                    ]

        # try:
        random_header = random.choice(my_headers)
        print "Random header     :", random_header
        response_html = requests.get(driver.current_url,random_header,verify=False)
        # except:
        #     print "download_by_virsual_agent Error,Error，Error，Error----------------------------"

        # 保存当前网页文档名为driver.title的txt格式文件,SaveHtmlFile(driver, response_html, path, fileTitleName)
        print driver.title
        print "aaaaaaaaaaaaaaaaaa"
        fileTitleName = driver.title + ".html"
        fn = open(fileTitleName,'w')  
        fn.write(response_html.content)
        print "Downloading Html:" ,fileTitleName
        fn.close()
        
        print response_html.status_code
        print response_html.text

        # Parse
        # 定义一个BeautifulSoup对象，传入的参数html.parser是什么意思？
        fileParser = "html.parser"
        parserEncoding = "utf-8"
        #soup = BeautifulSoup(response_html.text, fileParser, from_encoding=parserEncoding)

#        # 仅提取内容部分的文档，方便解析提速
        html_part_id_value =  "cards-holder"
        only_content_tags = SoupStrainer(id=html_part_id_value)
        # only_content_tags = SoupStrainer("div", id=html_part_id_value)
        html_part_content = BeautifulSoup(response_html.text, "html.parser", parse_only=only_content_tags).prettify()

        # 解析所需的所有链接
        soup = BeautifulSoup(html_part_content, "html.parser", from_encoding="utf-8")
        links = soup.find_all('a', href=re.compile("phone", re.I))
        
        #links = soup.find_all('a',class_='pstl') #, href=re.compile("Phone")
        for link in links:
            # 产生新的url的方式不同
            url_parse = urlparse(url)
            domain = url_parse.scheme + "://" + url_parse.netloc
            new_url = domain + link['href']
            handle_result_url(new_url, i)
            print "Fetch a phone url :",new_url
        i = i+1
        
        print "Done getinfo of   :",driver.current_url
        # nextPage = "a.jsNxtPage.pgNext"
        # driver.find_element_by_css_selector(nextPage).click()

        driver.find_element_by_xpath("//*[@id='pnnext']/span[2]").click()
        print "Get next url      :", driver.current_url
        time.sleep(3)

    # # 注意这里使用cssselect的a.next next必须为class类型
    # nextAttr = "next"
    # nextTag = "a." + nextAttr
    # driver.find_element_by_css_selector(nextTag).click()
    # print "Home Page:", driver.current_url

        # res_data = {}
        # head_node = soup.find("head")
        # res_data['tile'] = head_node.title.text

        # # 添加网页URL
        # res_data['url'] = driver.current_url
        # print res_data

    driver.quit()
 

def GetNewKeyWord():
    productArray = []
    file = open("Bikes.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        productArray.append(line)
    return  productArray

if __name__ == '__main__':

    db = DBMysql()

    # sql = 'select * from keyword_info'
    # results = db.query(sql, "all")
    # for r in results:
    #    item = keyword_Info_item()
    #    item.keyword =r[0]
    #    item.name = r[1]
    #    keyword_info_lists.append(item)

    # for i in keyword_info_lists:
    #     print i.keyword, i.name


    # productArray = GetNewKeyWord()
    # productArrayLen = len(productArray)
    # for i in range(productArrayLen):
    #　获取chrome driver
    driverPath = "D:\App\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverPath
    driver = webdriver.Chrome(driverPath)

        # 直接使用phantomjs虚拟浏览器
        #driver = webdriver.PhantomJS(executable_path="C:\Python27\Scripts\phantomjs.exe")
        # keyword = productArray[i].rstrip() + " 2016 news article"
        # print keyword
        
    keyword = "phone"
    url = "http://www.sears.com"
    
    print "Search info of    :", keyword
    print "Init url          :", url
    GetPage(driver, keyword, url)

    db.close

# todo 
# 使用BeautifulSoup获取新闻main/产品下的新闻框html标头，<div id="main">，或者产品框的产品框标头。<div id="Center" class="rr_present">
# 先翻页，然后使用使用BeautifulSoup的SoupStrainer获取局部xml，然后解析，解析出所有的url，
# 然后使用driever打开每一个url，获取网页链接，网页标题，获取网页，然后退回，
# 或者使用request继续处理，从url列表中不停的取出元素，进行处理
# 打开页面之后，加try catche，进行查找，匹配，
# 对于新闻，匹配关键字
# 对于商品，匹配关键字，价格等


# 1！ 针对扫描到的网页url，使用driver或者request打开，判断是否是死链接，然后用baautifulsoup提取主要框内的文本，然后遍历其中的链接，判断链接是否正常，并判断具体信息
# 判断数据库是否可用
# 实现将数据加载到数据库表中
# 将新闻的所有内容抓取到库中
# 将产品的内容，抓到多个网站中

# 设计数据库表
# 设计类，宽泛类

# 1 从数据库导入关键字信息，进行跳转页框
# 2 从文本文件导入关键字信息，进行跳转页框  -> 主网页一个表 关键字一个表，作为类目 -> 具体产品或者搜素对象一个表->
# 3 设计数据库
# 4 





    # 下载新闻的时候，直接使用那个串，而不是去读取。
    # 大量使用正则表达式筛选内容
    # 新闻：可以找门户网站
    # 电商，可以翻页，或者按模块找
    # 可以找谷歌商品

    # GetPage中，使用xpath方法获取下一页标记，应该行，结果不行
    # driver.find_element_by_xpath("//a[@class='next']").click() 或
    #elem = driver.find_element_by_xpath("//a[contains(text(),'next')]")
    # print driveurrent_url


    # 注意这里使用cssselect的a.next next必须为class类型
    # driver.find_element_by_css_selector("a._blank").click()
    # print driver.current_url
    # print "_bank"


    # next = driver.find_element_by_class_name("next")
    # next_url = next.get_attribute("href")
    # print new_url.text

    
    # elem = driver.find_element_by_xpath("//*[@id=""yui_3_10_0_1_1474860908632_380""]")
    # print elem
    # print "okkkkkkk"
    # # 所有的标题都在这个标签下的ol - li标签下
    # div = driver.find_elements_by_id("web")
    # print div
    # #wrong : ol = driver.find_element_by_id("yui_3_10_0_1_1474860908632_363")
    # print ol.get_attribute("id")
    # lis = driver.find_elements_by_tag_name("li")
    # for li in lis:
    #     print li.get_attribute("id")

    # links = driver.find_elements_by_tag_name("a")
    # for link in links:
    #     try:    
    #         href = link.get_attribute("href")    
    #         target = link.get_attribute('target')
    #         print href, target
    #         if target == "_blank":
    #             print href
    #     except:
    #         print "ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"


    # my_headers = [
    #             "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
    #             "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
    #             "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
    #             "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
    #             ]

    # try:
    #     req = urllib2.Request(driver.current_url)

    #     proto, rest = urllib2.splittype(driver.current_url) 
    #     host, rest = urllib2.splithost(rest) 
    #     random_header = random.choice(my_headers)

    #     req.add_header("User-agent", random_header)
    #     req.add_header("Host", host)
    #     req.add_header("Referer", host)
    #     req.add_header("GET",driver.current_url)
    #     response_html = urllib2.urlopen(req)
    #     print response_html
    #     print "-------------------------------------------------------------------------------------------------------------------"
    # except:
    #     print "download_by_virsual_agent Error,Error，Error，Error----------------------------"
    #     print driver.current_url
    # else:
    #     print "download_by_virsual_agent Ok，Ok，Ok，Ok，Ok，Ok-------------------------------"
    #     print driver.current_url
    # print "ok"

    # url = 'http://www.jianshu.com/users/65ed1c462691/top_articles'
    # header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
    # response = requests.get(url, headers=header)
