# coding=utf-8
import uuid
import pymysql
import datetime


def insert_webpage(id, title, url, content):
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='baike_science',
        use_unicode=True,
        charset="utf8"
    )
    # 获取游标
    cur = conn.cursor()
    # 插入数据，注意看有变量的时候格式
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    # cur.execute("SET character_set_client = gbk")
    # cur.execute("SET character_set_results = gbk")
    cur.execute("INSERT INTO webpage(id,title,url,content,time_stamp) VALUES (%s,%s,%s,%s, %s)",
                (id, title, url, content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # 提交
    cur.close()
    conn.commit()
    # 关闭连接
    conn.close()


def insert_relationship(src_id, src_title, des_id, des_title):
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='baike_science',
        use_unicode=True,
        charset="utf8"
    )
    # 获取游标
    cur = conn.cursor()
    # 插入数据，注意看有变量的时候格式
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    # cur.execute("SET character_set_client = gbk")
    # cur.execute("SET character_set_results = gbk")
    id = str(uuid.uuid1())
    cur.execute("INSERT INTO relationship(id,src_id,src_title,des_id,des_title,time_stamp) VALUES (%s,%s,%s,%s,%s,%s)",
                (id, src_id, src_title, des_id, des_title, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # 提交
    cur.close()
    conn.commit()
    # 关闭连接
    conn.close()


def insert_attributes(entity_id, entity_title, names_lists_insert, value_lists_insert):
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        database='baike_science',
        use_unicode=True,
        charset="utf8"
    )
    # 获取游标
    cur = conn.cursor()
    # 插入数据，注意看有变量的时候格式
    cur.execute('SET NAMES utf8mb4')
    cur.execute("SET CHARACTER SET utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    # cur.execute("SET character_set_client = gbk")
    # cur.execute("SET character_set_results = gbk")
    id = str(uuid.uuid1())
    cur.execute("INSERT INTO attribute(id,entity_id,entity_title,attribute_name,attribute_value,time_stamp) VALUES (%s,%s,%s,%s,%s,%s)",
                (id, entity_id, entity_title, names_lists_insert, value_lists_insert, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    # 提交
    cur.close()
    conn.commit()
    # 关闭连接
    conn.close()
