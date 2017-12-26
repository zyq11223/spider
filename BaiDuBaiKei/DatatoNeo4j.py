# -*- coding: utf-8 -*-
# author：wxm

import pandas as pd
import pymysql
from py2neo import Graph,Node,Relationship
import csv

## 加上字符集参数，防止中文乱码
def get_items_from_database():
    #链接数据库
    dbconn = pymysql.connect(
    host="192.168.1.24",
    database="baike_science",
    user="root",
    password="root",
    port=3306,
    charset='utf8',
    use_unicode=True,
    )

    # # sql语句
    # sqlcmd = "SELECT id,title,url FROM webpage WHERE time_stamp < '2017-12-21 00:00:00' "
    #
    # # 利用pandas 模块导入mysql数据
    # data= pd.read_sql(sqlcmd, dbconn) #python pandas.core.frame.DataFrame类型

    #链接neo4j
    test_graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="780961"
    )
    #清空数据库
    test_graph.delete_all()

    #get items form relationship表
    # sqlcmd_relationship = "SELECT src_id,src_title,des_id,des_title FROM relationship WHERE src_id = '2f18ef43-d854-34f9-a64c-a7e22074ab5f' "
    sqlcmd_relationship = "SELECT src_id,src_title,des_id,des_title FROM relationship WHERE time_stamp < '2017-12-20 23:33:52' "
    # sqlcmd_attribute="select entity_title,attribute_name,attribute_value from attribute WHERE time_stamp < '2017-12-20 23:33:52'"
    relationship= pd.read_sql(sqlcmd_relationship, dbconn)  # python pandas.core.frame.DataFrame类型
    # attribute=pd.read_sql(sqlcmd_attribute, dbconn)



    for indexs_2 in relationship.index:
        relationship_lists = relationship.loc[indexs_2].values[0:]
        print(relationship_lists[1],relationship_lists[3])
      # 分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"CALL"，两条关系都有属性count，且值为1
    #判断记录是否存在，避免插入重复结点
        existing_node1 = test_graph.find_one(label=relationship_lists[1])#1:src_title
        existing_node2 = test_graph.find_one(label=relationship_lists[3]) #3:des_title
        #如果src_title存在：
        if existing_node1:
            #如果des_title存在
            if existing_node2:
                src_call_des = Relationship(existing_node1, 'link', existing_node2)
            else:
                print("ok3")
                test_node_2 = Node(relationship_lists[3], name=relationship_lists[3])
                sqlcmd_attribute2 = "select entity_title,attribute_name,attribute_value from attribute WHERE entity_id = '" + \
                                    relationship_lists[2] + "'" #des_id
                attribute = pd.read_sql(sqlcmd_attribute2, dbconn)
                # 获取属性
                for index_1 in attribute.index:
                    attribute_lists = attribute.loc[index_1].values[0:]
                    test_node_2[attribute_lists[1]] = attribute_lists[2]
                test_graph.create(test_node_2)
                src_call_des = Relationship(existing_node1, 'link', test_node_2)
                src_call_des['count'] = 1
            test_graph.create(src_call_des)
        else:
            test_node_1 = Node(relationship_lists[1], name=relationship_lists[1])
            sqlcmd_attribute1 = "select entity_title,attribute_name,attribute_value from attribute WHERE entity_id = '" + \
                                relationship_lists[0] + "'"
            attribute = pd.read_sql(sqlcmd_attribute1, dbconn)
            ##获取属性
            for index_1 in attribute.index:
                attribute_lists = attribute.loc[index_1].values[0:]
                test_node_1[attribute_lists[1]] = attribute_lists[2]
            test_graph.create(test_node_1)

            if existing_node2:
                src_call_des = Relationship(test_node_1, 'link', existing_node2)
            else:
                print("ok2")
                test_node_2 = Node(relationship_lists[3], name=relationship_lists[3])
                sqlcmd_attribute2 = "select entity_title,attribute_name,attribute_value from attribute WHERE entity_id = '" + \
                                    relationship_lists[2] + "'"
                attribute = pd.read_sql(sqlcmd_attribute2, dbconn)
                ##获取属性
                for index_1 in attribute.index:
                    attribute_lists = attribute.loc[index_1].values[0:]
                    test_node_2[attribute_lists[1]] = attribute_lists[2]
                test_graph.create(test_node_2)

                src_call_des = Relationship(test_node_1, 'link', test_node_2)
                src_call_des['count'] = 1
            test_graph.create(src_call_des)



# def connect_neo4j():
#     test_graph = Graph(
#         "http://localhost:7474",
#         username="neo4j",
#         password="780961"
#     )
#     test_graph.delete_all()
#     #建立节点的时候要定义它的节点类型（label）以及一个基本属性（property，包括property_key和property_value）
#     test_node_1 = Node("Person", name="test_node_1")
#     test_node_2 = Node("Person", name="test_node_2")
#     # test_graph.create(test_node_1)
#     # test_graph.create(test_node_2)    # test_graph = Graph(
#     #     "http://localhost:7474",
#     #     username="neo4j",
#     #     password="780961"
#     # )
#     # test_graph.delete_all()
#     # #建立节点的时候要定义它的节点类型（label）以及一个基本属性（property，包括property_key和property_value）
#     # test_node_1 = Node(label="Person", name="test_node_1")
#     # test_node_2 = Node(label="Person", name="test_node_2")
#     # test_graph.create(test_node_1)
#     # test_graph.create(test_node_2)
#     # #分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"CALL"，两条关系都有属性count，且值为1
#     # node_1_call_node_2 = Relationship(test_node_1, 'CALL', test_node_2)
#     # node_1_call_node_2['count'] = 1
#     # node_2_call_node_1 = Relationship(test_node_2, 'CALL', test_node_1)
#     # node_2_call_node_1['count'] = 2
#     # test_graph.create(node_1_call_node_2)
#     # test_graph.create(node_2_call_node_1)
#
#     test_graph.create(test_node_1)
#     test_graph.create(test_node_2)
#
#     node_1_call_node_2 = Relationship(test_node_1, 'CALL', test_node_2)
#     node_2_call_node_1 = Relationship(test_node_2, 'CALL', test_node_1)
#     test_graph.create(node_1_call_node_2)
#     test_graph.create(node_2_call_node_1)
#
#     find_code_1 = test_graph.find_one(
#         label="Person",
#         property_key="name",
#         property_value="test_node_1"
#     )
#     print(find_code_1)
#
# def put_attribute_into_items():
#     dbconn = pymysql.connect(
#         host="192.168.1.24",
#         database="baike_science",
#         user="root",
#         password="root",
#         port=3306,
#         charset='utf8',
#         use_unicode=True,
#     )
#     # 获取游标
#     cur = dbconn.cursor()
#     # 插入数据，注意看有变量的时候格式
#     cur.execute("select entity_title,attribute_name,attribute_value from attribute WHERE time_stamp < '2017-12-21 02:00:00'")
#     data = cur.fetchall()
#     # 提交
#     cur.close()
#     dbconn.commit()
#     # 关闭连接
#     dbconn.close()
#     return data

if __name__ == '__main__':
    items_data=get_items_from_database()




