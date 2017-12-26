# -*- coding:UTF-8 -*-
# Leaning：
# 类的静态变量：使用双下划线开头
# 类的私有变量：使用单下划线开头

# 类的公有函数：开头无下划线
# 类的私有函数：双下划线开头

import time
import threading
import MySQLdb
from DBUtils import PooledDB

class DBManager(object):
    __pool = None

    def __init__(self):
        self._conn = self.__get_conn()
        self._cursor = self._conn.cursor()

    def __get_conn(self):
        if self.__pool is None:
            __pool = PooledDB.PooledDB(MySQLdb,100,50,100,490,False,host='127.0.0.1',user='root',passwd='',db='0Spider',charset='utf8')
        return __pool.connection()

    def get_all(self, sql,param = None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.excute(sql,param)

        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def get_one(self, sql, param=None):
        if param is 
    

    def end(self, option = 'commit'):
        if option == 'commit':
            self._conn.commit()
        elif option == 'rollback':
            self._conn.rollback()

    def dispose(self, isEnd = 1):
        if isEnd == 1:
            self.end('commit')
        elif isEnd == 0:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()

pool = PooledDB.PooledDB(MySQLdb,100,50,100,490,False,host='127.0.0.1',user='root',passwd='',db='0Spider',charset='utf8')

class MyThread(threading.Thread):
    def __init__(self,threadName):
        # self.conn = pool.connection()
        self._db_manager = DBManager()
        threading.Thread.__init__(self,name=threadName)
        print "MyThread"

    def run(self):
        #cursor = self.conn.cursor()
        print "hello-->",self.getName()
        file_object = open('8.txt','a+')
        file_object.write(self.getName()+'\n')
        file_object.close()
        print self._db_manager.get_all("select * from keyword_info")
        self._db_manager.dispose(1)
        #print cursor.execute("select * from keyword_info;")
        # self.conn.commit()
        time.sleep(10)

    def __del__(self):
        pass
        # self.conn.close()
        # self.conn = None

for i in range(5):
    obj = MyThread(str(i))
    obj.start()

# db_manage = DBManager()
# print db_manage.get_all("select * from keyword_info")


