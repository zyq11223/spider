# -*- coding:UTF-8 -*-

import MYSQLdb
import requests
from bs4 import BeautifulSoup
import time
import re

def dbstatus(user,pwd):#检测数据库proxy状态，无则创建。
    conn=pymysql.connect(host='127.0.0.1',user=user,passwd=pwd,charset='utf8')
    cur=conn.cursor()
    conn.select_db('information_schema')
    dbstat=cur.execute('SELECT * from SCHEMATA where SCHEMA_NAME="0spider"')
    if dbstat==0:
        print('数据库不存在，正在创建数据库...')
        cur.execute("CREATE DATABASE proxy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")#添加proxy数据库，默认utf8
        conn.select_db('proxy')
        print('创建temp表...')
        cur.execute("""
                     CREATE TABLE `temp` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `ip` varchar(255) COLLATE utf8_bin NOT NULL,
                    `port` varchar(255) COLLATE utf8_bin NOT NULL,
                    `place` varchar(255) COLLATE utf8_bin,
                    `iptype` varchar(255) COLLATE utf8_bin NOT NULL,
                    `time` varchar(255) COLLATE utf8_bin NOT NULL,
                    PRIMARY KEY (`id`)
                  )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;
                    """)
        print('创建temp表成功')
        print('创建iptable表...')
        cur.execute("""
                     CREATE TABLE `iptable` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `ip` varchar(255) COLLATE utf8_bin NOT NULL,
                    `port` varchar(255) COLLATE utf8_bin NOT NULL,
                    `place` varchar(255) COLLATE utf8_bin,
                    `iptype` varchar(255) COLLATE utf8_bin NOT NULL,
                    `time` varchar(255) COLLATE utf8_bin NOT NULL,
                    PRIMARY KEY (`id`)
                  )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;
                    """)
        print('创建iptable表成功')
        print('创建完成')
    cur.close()

def xicidaili():#将西刺代理的数据入库
    nows=time.time()
    home='http://www.xicidaili.com'
    guonei='http://www.xicidaili.com/nn/'
    guowai='http://www.xicidaili.com/wn/'
    def getiplist(url):
        count=0
        sql="INSERT INTO ip_proxiex(ip,port,place,iptype,time) VALUES (%s,%s,%s,%s,%s)"
        headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
        }
        conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='proxy',charset='utf8')
        cur=conn.cursor()
        s = requests.session()
        res = s.get(url, headers=headers_base)
        ipsoup=BeautifulSoup(res.content.decode('utf8'), "html.parser")
        nextpagetgae=ipsoup.find_all(attrs={'class':'next_page'})
        while nextpagetgae!=[]:
            iptable=ipsoup.find(attrs={'id':'ip_list'})
            iplist=iptable.find_all('tr')
            for i in iplist[1:]:
                ipinfo=i.find_all(name='td')
                ip=ipinfo[1].string
                port=ipinfo[2].string
                place=ipinfo[3].string
                iptype=ipinfo[5].string
                updatetime='20'+ipinfo[9].string
                t=(int(updatetime[:4]),int(updatetime[5:7]),int(updatetime[8:10]),int(updatetime[11:13]),int(updatetime[14:16]),0,0,0,0)
                updatetimes=time.mktime(t)
                if nows+28800-updatetimes>86400*1:#如果更新时间与现时间差超过X天则丢弃,28800是为了纠正东八区的8小时时差,86400是一天
                    conn.commit()
                    cur.close()
                    print('导入%d条数据'%count)
                    return
                if place==None:
                    place=ipinfo[3].a.string
                cur.execute(sql,[ip,port,place.strip(),iptype,updatetime])
                count+=1
            conn.commit()
            if nextpagetgae[0].get('href')==None:
                break
            nextpage=home+nextpagetgae[0].get('href')
            ipsoup=BeautifulSoup(s.get(nextpage,headers=headers_base).content.decode('utf8'), "html.parser")
            nextpagetgae=ipsoup.find_all(attrs={'class':'next_page'})
        cur.close()
        print('导入%d条数据'%count)
    getiplist(guonei)
    getiplist(guowai)




#dbstatus('root','')    
xicidaili()

# import urllib2
# import cookielib
# import lxml.html
# import threading
# import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# from __builtin__ import False

# ip_list = [] # 最后的可用列表
# def prepare():
#     cj = cookielib.MozillaCookieJar()
#     cookie_support = urllib2.HTTPCookieProcessor(cj)
#     opener = urllib2.build_opener(cookie_support)
#     opener.addheaders =  [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')]
#     urllib2.install_opener(opener)

# def page(j):
#     prepare()
#     try:
#         url = 'http://www.xicidaili.com/wn/' + str(j)
#         response = urllib2.urlopen(url)
#         http = response.read().decode('utf-8')
#         doc = lxml.html.fromstring(http)
#         results = doc.xpath('//div/table[@id="ip_list"]/tr/td/text()')
#         return  results
#     except:
#         pass

# def page_contenet(j):
#     url = 'http://www.xicidaili.com/wn/'+str(j)
#     results = page(j)
#     for i in range(1, 100):
#         try:
#             proxy = results[i*10] + ":" + results[i*10 + 1]
#             sContent = urllib2.urlopen(url, timeout = 3).getcode()
#             if(sContent == 200):
#                 print proxy
#                 ip_list.append(proxy)
#             else:
#                 print ("the url geted now is invalid!")
#         except:
#             pass

# class everpage(threading.Thread):
#     def __init__(self, page):
#         threading.Thread.__init__(self)
#         self.page = page
#         self.thread_stop = False

#     def run(self):
#         while not self.thread_stop:
#             page_contenet(self.page)
#             self.stop()

#     def stop(self):
#         self.thread_stop = True

# if __name__ == '__main__':
#     for i in range(1, 100):
#         try:
#             e = everpage(i)
#             e.start()
#             time.sleep(5)
#         except:
#             pass


# 一年前突然有个灵感，想搞个强大的网盘搜索引擎，但由于大学本科学习软件工程偏嵌入式方向，web方面的能力有点弱，不会jsp，不懂html，好久没有玩过sql，但就是趁着年轻人的这股不妥协的劲儿，硬是把以前没有学习的全部给学了一遍，现在感觉web原来也就那么回事。好了，废话就不说了，看到本文的读者，可以先看看我做的东西：
# 去转盘网：www.quzhuanpan.com
# ok搜搜：www.oksousou.com（这个是磁力，顺便拿出来给大伙观赏）
# 言归正传，由于我要爬取百度网盘，而度娘你懂的的搞爬虫出生的，反爬虫的能力很牛掰。尤其像我用我的电脑去爬百度网盘，爬几天百度就盯上了我的机子，爬虫开始爬不出东西。之后网上东查，西查，发现可以通过代理来解决这个问题，所以又去爬代理。我爬的是这个网站：
# http://www.xicidaili.com/ 之后他貌似他开始反击，我又将魔爪指向了：http://www.kuaidaili.com。
# 想必看这篇博文的多半是程序猿，所以还是先上代码(我会写注释的，放心，该爬虫以http://www.xicidaili.com/为目标):
#coding:utf-8
import json
import sys
import urllib, urllib2
import datetime
import time
reload(sys)
sys.setdefaultencoding('utf-8') 
from Queue import Queue
from bs4 import BeautifulSoup
import MySQLdb as mdb
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = 'root'
ID=0
ST=1000
uk='3758096603'
classify="inha"
proxy = {u'https':u'118.99.66.106:8080'}

class ProxyServer:
    def __init__(self): #这个就不说了，数据库初始化，我用的是mysql
        self.dbconn = mdb.connect(DB_HOST, DB_USER, DB_PASS, 'ebook', charset='utf8')
        self.dbconn.autocommit(False)
        self.next_proxy_set = set()
        self.chance=0
        self.fail=0
        self.count_errno=0
        self.dbcurr = self.dbconn.cursor()
        self.dbcurr.execute('SET NAMES utf8')
        
    def get_prxy(self,num): #这个函数用来爬取代理
        while num>0:
            global proxy,ID,uk,classify,ST
            count=0
            for page in range(1,718): #代理网站总页数，我给了个718页
                if self.chance >0: #羊毛出在羊身上，如过爬取网站开始反击我，我就从他那爬下来的
                #代理伪装，这个self.chance表示我什么时候开始换代理
                    if ST % 100==0:
                        self.dbcurr.execute("select count(*) from proxy")
                        for r in self.dbcurr:
                            count=r[0]
                        if ST>count:
                            ST=1000 #我是从数据库的第1000条开始换的，这段你可以改，搞个随机函数随机换，我写的很简单
                    self.dbcurr.execute("select * from proxy where ID=%s",(ST))
                    results = self.dbcurr.fetchall()
                    for r in results:
                        protocol=r[1]
                        ip=r[2]
                        port=r[3]
                        pro=(protocol,ip+":"+port)
                        if pro not in self.next_proxy_set:
                            self.next_proxy_set.add(pro)
                    self.chance=0
                    ST+=1
                proxy_support = urllib2.ProxyHandler(proxy) #注册代理
                # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))
                opener = urllib2.build_opener(proxy_support)
                urllib2.install_opener(opener)
                #添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
                # i_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
                i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
                #url='http://www.kuaidaili.com/free/inha/' + str(page)
                url='http://www.kuaidaili.com/free/'+classify+'/' + str(page)
                html_doc=""
                try:
                    req = urllib2.Request(url,headers=i_headers)
                    response = urllib2.urlopen(req, None,5)
                    html_doc = response.read() #这不就获取了要爬取的页面嘛？
                except Exception as ex: #看抛出异常了，可能开始反击我，我开始换代理
                    print "ex=",ex
                    pass
                    self.chance+=1
                    if self.chance>0:
                        if len(self.next_proxy_set)>0:
                            protocol,socket=self.next_proxy_set.pop()
                            proxy= {protocol:socket}
                            print "proxy",proxy
                            print "change proxy success."
                    continue
                #html_doc = urllib2.urlopen('http://www.xici.net.co/nn/' + str(page)).read()
                if html_doc !="": #解析爬取的页面，用的beautifulSoup
                    soup = BeautifulSoup(html_doc,from_encoding="utf8")
                    #print "soup",soup
                    #trs = soup.find('table', id='ip_list').find_all('tr') #获得所有行
                    trs = ""
                    try:
                        trs = soup.find('table').find_all('tr')
                    except:
                        print "error"
                        continue
                    for tr in trs[1:]:
                        tds = tr.find_all('td')
                        ip = tds[0].text.strip() #ip
                        port = tds[1].text.strip() #端口
                        protocol = tds[3].text.strip()
                        #tds = tr.find_all('td')
                        #ip = tds[2].text.strip()
                        #port = tds[3].text.strip()
                        #protocol = tds[6].text.strip()
                        get_time= tds[6].text.strip()
                        #get_time = "20"+get_time
                        check_time = datetime.datetime.strptime(get_time,'%Y-%m-%d %H:%M:%S')
                        temp = time.time()
                        x = time.localtime(float(temp))
                        time_now = time.strftime("%Y-%m-%d %H:%M:%S",x) # get time now,入库时间
                        http_ip = protocol+'://'+ip+':'+port
                        if protocol == 'HTTP' or protocol == 'HTTPS': #只要http协议相关代理，其他一律不要
                            content=""
                            try: #我就是不放心这个网站，所以爬下来后我又开始检测代理是否真的有效
                                proxy_support=urllib2.ProxyHandler({protocol:http_ip})
                                # proxy_support = urllib2.ProxyHandler({'http':'http://124.200.100.50:8080'})
                                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                                urllib2.install_opener(opener)
                                if self.count_errno>50:
                                    self.dbcurr.execute("select UID from visited where ID=%s",(ID)) #这是我的数据库，我取了一个叫uk的东东，这个
                                    你不用管，你想检测拿你要爬取的链接检测代理吧
                                    for uid in self.dbcurr:
                                        uk=str(uid[0])
                                    ID+=1
                                    if ID>50000:
                                        ID=0
                                    self.count_errno=0
                                test_url="http://yun.baidu.com/pcloud/friend/getfanslist?start=0&query_uk="+uk+"&limit=24" #我用来检测的链接
                                print "download:",http_ip+">>"+uk
                                req1 = urllib2.Request(test_url,headers=i_headers)
                                response1 = urllib2.urlopen(req1, None,5)
                                content = response1.read()
                            except Exception as ex: #抛异常后的处理
                                #print "ex2=",ex
                                pass
                                self.fail+=1
                                if self.fail>10:
                                    self.fail=0
                                    break
                                continue
                            if content!="": 
                                json_body = json.loads(content)    
                                errno = json_body['errno']  
                                self.count_errno+=1 
                                if errno!=-55: #检验该代理是有用的，因为content！="" 并且度娘返回not -55
                                    print "success."
                                    self.dbcurr.execute('select ID from proxy where IP=%s', (ip)) #开始入库了
                                    y = self.dbcurr.fetchone()
                                    if not y:
                                        print 'add','%s//:%s:%s' % (protocol, ip, port)
                                        self.dbcurr.execute('INSERT INTO proxy(PROTOCOL,IP,PORT,CHECK_TIME,ACQ_TIME) VALUES(%s,%s,%s,%s,%s)',(protocol,ip,port,check_time,time_now))
                                        self.dbconn.commit()
            num-=1
            if num % 4 ==0:
                classify="intr" #这个是原来网站的那几个标签栏名称，我是一栏一栏的爬取的
            if num % 4 ==1:
                classify="outha"
            if num % 4 ==2:
                classify="outtr"
            if num % 4 ==3:
                classify="inha"
