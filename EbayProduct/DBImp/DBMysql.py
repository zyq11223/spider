#-*- coding:utf-8 -*-
import MySQLdb

from DBImp.DBConfig import DBConfig


class DBMysql(object):
    _dbConfig   = None
    _cursor     = None
    _connect    = None
    _error_code = ''

    TIMEOUT_DEADLINE = 30 # quit connect if beyond 30S
    TIMEOUT_THREAD = 10 # threadhold of one connect
    TIMEOUT_TOTAL = 0 # total time the connects have waste


    def escape_string(self,stringData):
        return self._connect.escape_string(stringData.encode('utf-8'))

    def __init__(self):
        try:
            self._dbConfig = DBConfig
            self.dbconfig_test(self._dbConfig)
            self._connect  = MySQLdb.connect(host    = self._dbConfig['host'],
                                             port    = self._dbConfig['port'],
                                             user    = self._dbConfig['user'],
                                             passwd  = self._dbConfig['passwd'],
                                             db      = self._dbConfig['db'],
                                             charset = self._dbConfig['charset'],
                                             connect_timeout=self.TIMEOUT_THREAD
                                             )
            print "ok"
        except MySQLdb.Error, e:
            self._error_code = e.args[0]
            error_msg = "%s --- %s" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), type(e).__name__), e.args[0], e.args[1]
            print "Error", error_msg

            # reconnect if not reach TIMEOUT_DEADLINE.
            if self.TIMEOUT_TOTAL < self.TIMEOUT_DEADLINE:
                interval = 0
                self.TIMEOUT_TOTAL += (interval + self.TIMEOUT_THREAD)
                time.sleep(interval)
                return self.__init__()
                print "Error"
            raise Exception(error_msg)

        self._cursor = self._connect.cursor()

    def dbconfig_test(self,dbConfig):
        flag = True
        if type(dbConfig) is not dict:
            print 'dbConfig is not dict'
            flag = False
        else:
            for key in ['host','port','user','passwd','db']:
                if not dbConfig.has_key(key):
                    print "dbConfig error: do not have %s" % key
                    flag = False
            if not dbConfig.has_key('charset'):
                self._dbconfig['charset'] = 'utf8'

        if not flag:
            raise Exception('Dbconfig Error')
        return flag


    def query(self, sql, ret_type='all'):
            try:
                self.__init__()
                self._cursor.execute("SET NAMES utf8")
                results = self._cursor.execute(sql)
                if ret_type == 'all':
                    return self._cursor.fetchall()
                    # return self.rows2array(self._cursor.fetchall())
                elif ret_type == 'one':
                    return self._cursor.fetchone()
                elif ret_type == 'count':
                    return self._cursor.rowcount
            except MySQLdb.Error, e:
                self._error_code = e.args[0]
                print "Mysql execute error:",e.args[0],e.args[1]
                return False


    def dml(self, sql):
        '''update or delete or insert'''
        try:
            self.__init__()
            self._cursor.execute("SET NAMES utf8")
            self._cursor.execute(sql)
            self._connect.commit()
            type = self.dml_type(sql)
            # if primary key is auto increase, return inserted ID.
            if type == 'insert':
                return self._connect.insert_id()
            else:
                return True
        except MySQLdb.Error, e:
            self._error_code = e.args[0]
            print "Mysql execute error:",e.args[0],e.args[1]
            return False

    # 可以插入、删除、更新操作
    def dml_type(self, sql):
        self.__init__()
        re_dml = re.compile('^(?P<dml>\w+)\s+', re.I)
        m = re_dml.match(sql)
        if m:
            if m.group("dml").lower() == 'delete':
                return 'delete'
            elif m.group("dml").lower() == 'update':
                return 'update'
            elif m.group("dml").lower() == 'insert':
                return 'insert'
        print "%s --- Warning: '%s' is not dml." % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), sql)
        return False

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #插入数据
    def insertData(self, table, my_dict):
        try:
            self.__init__()
            self._connect.set_character_set('utf8')
            cols = ', '.join(my_dict.keys())
            values = '"," '.join(str(my_dict.values()))
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
            try:
             result = self._cursor.execute(sql)
             insert_id = self._connect.insert_id()
             self._cursor.commit()
             #判断是否执行成功
             if result:
                 return insert_id
             else:
                 return 0
            except MySQLdb.Error,e:
            
                # #发生错误时回滚
                # self._cursor.rollback()
                #主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print self.getCurrentTime(),"数据已存在，未插入数据"
                else:
                    print self.getCurrentTime(),"插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
        except MySQLdb.Error,e:
            print self.getCurrentTime(),"数据库错误，原因%d: %s" % (e.args[0], e.args[1])

    # def rows2array(self, data):
    #     '''transfer tuple to array.'''
    #     result = []
    #     for da in data:
    #         if type(da) is not dict:
    #             raise Exception('Format Error: data is not a dict.')
    #         print da
    #         result.append(da)
    #     return result

     #插入数据
    def insertOneData(self, table, my_dict):
        try:
            self._connect.set_character_set('utf8')
            cols = ', '.join(my_dict.keys())
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
            try:
                result = self._cursor.execute(sql)
                insert_id = self._connect.insert_id()
                self._connect.commit()
                #判断是否执行成功
                if result:
                    print "DB Model: Success Insert One Data!"
                    return insert_id
                else:
                    return 0
            except MySQLdb.Error,e:
             #发生错误时回滚
             self._connect.rollback()
             #主键唯一，无法插入
             if "key 'PRIMARY'" in e.args[1]:
                 print self.getCurrentTime(),"数据已存在，未插入数据"
             else:
                 print self.getCurrentTime(),"插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
        except MySQLdb.Error,e:
            print self.getCurrentTime(), "DB Model: Error，Reason%d: %s" % (e.args[0], e.args[1])
            self.__init__()
            self.insertOneData(table, my_dict)

    def insert(self,table_name,data):
        self.__init__()
        columns=data.keys()
        _prefix="".join(['INSERT INTO `',table_name,'`'])
        _fields=",".join(["".join(['`',column,'`']) for column in columns])
        _values=",".join(["%s" for i in range(len(columns))])
        _sql="".join([_prefix,"(",_fields,") VALUES (",_values,")"])
        print "n"
        print "n"
        print "n"
        print _sql
        print "n"
        print "n"
        print "n"
        _params=[data[key] for key in columns]

        self._cursor.execute(_sql,tuple(_params))

        self._connect.commit()
        type = self.dml_type(_sql)
        # if primary key is auto increase, return inserted ID.
        if type == 'insert':
            return self._connect.insert_id()
        else:
            return True
                        
    def update(self,tbname,data,condition):
        self.__init__()
        _fields=[]
        _prefix="".join(['UPDATE `',tbname,'`','SET'])
        for key in data.keys():
            _fields.append("%s = %s" % (key,data[key]))
        _sql="".join([_prefix ,_fields, "WHERE", condition ])
                            
        return self._cursor.execute(_sql)
                        
    def delete(self,tbname,condition):
        _prefix="".join(['DELETE FROM  `',tbname,'`','WHERE'])
        _sql="".join([_prefix,condition]) 
        return self._cursor.execute(_sql)

    def close(self):
        '''free source.'''
        try:
            self._cursor.close()
            self._connect.close()
        except:
            pass

    def rollback(self):
        self._cursor.rollback()

class keyword_Info_item:
    def __init__(self):
        self.keyword = ''     # 名称
        self.name = ''     # 尺寸

keyword_info_lists = []

import re
import time
import requests
import random
from bs4 import BeautifulSoup
from DBMysql import DBMysql
import uuid
from urlparse import urlparse


if __name__=='__main__':

    db = DBMysql()
    #db._init_()

    


    # sql_insert = "insert into keyword_info (keyword,name) value('1','2')"
    # db.dml(sql_insert)

    url = "https://search.yahoo.com/search?p=Merida+2016+news+article&fr=uh3_news_web_gs&fr2=p%3Anews%2Cm%3Asb"
    i = 1 

    my_headers = [
                "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
                "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
                "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
                ]

    # try:
    random_header = random.choice(my_headers)
    response_html = requests.get(url,random_header)

    if response_html.status_code == 200:
        fileParser = "html.parser"
        html_content = BeautifulSoup(response_html.text, fileParser)#以及编码值
        print html_content.title
        print "handle_selected_url", url, i

        url_parse = urlparse('http://blog.ourren.com/2015/04/14/ip-information-with-python/')
        domain = url_parse.scheme + "://www." + url_parse.netloc
        keyword = "bike"

        #构造用来插入数据的字典
        new_reconrd = {"id":str(uuid.uuid4()),
                       "domain_name":domain,
                       "keyword":keyword,
                       "url":url,
                       "title":html_content.title,
                       "doc":db.escape_string(unicode(response_html.text))
                    }

        # record = "INSERT INTO 0spider.online_product_news_data(id, domain_name, keyword, url, title, doc)VALUES ( " + "\"" + str(uuid.uuid4()) + "\"" + ", " + "\"" + domain + "\"" + ", " + "\"" + keyword +"\"" + ", "+ "\"" + url +"\"" + ", " + "\"" + str(html_content.title) + "\"" +", " + "\"" + db.escape_string(unicode(response_html.text)) +  "\"" + ")" 

        # str(html_content)

        db.insert("online_product_news_data",new_reconrd)
        # db.dml(record)

    db.close

# # 打开数据库连接
# db = MySQLdb.connect(host='127.0.0.1',user= 'root',passwd='',db='0Spider')
# db.autocommit(1)

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # 查询数据
# sql = 'select keyword,name from keyword_info'
# cursor.execute(sql)
# results = cursor.fetchall()
# for r in results:
#    item = keyword_Info_item()
#    item.keyword =r[0]
#    item.name = r[1]
#    keyword_info_lists.append(item)

# for i in keyword_info_lists:
#     print i.keyword, i.name

# # 插入数据
# #sql_insert = "insert into keyword_info (keyword,name) value('1','2')"

# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()
# cursor.close()
# db.close()
