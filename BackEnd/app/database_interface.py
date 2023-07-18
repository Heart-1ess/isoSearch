# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:39:59 2023

@author: 86136
"""

"""
    本模块提供了服务端操作MySQL数据库的接口。
"""

import pymysql

db_connection: pymysql.Connection
cursors: pymysql.cursors.Cursor
sql_index = 'select * from methods_demo'


def database_prepare():
    global db_connection
    global cursors
    db_connection = pymysql.connect(
        host='localhost',
        user='root',
        password='saoduankoushabi',
        database='isomerization_search',
        charset='utf8'
    )
    cursors = db_connection.cursor()
  
def is_index_existing(table: str, index: str) -> bool:
    """
    检查指定表内的指定索引是否存在

    :param table: 待查索引所对应表
    :param index: 待查索引
    :return: 若存在返回True，若不存在返回False
    """

    db_connection.ping(reconnect=True)
    cursors.execute(sql_index)
    db_connection.commit()
    sql = "SELECT * FROM %s" %table + " WHERE _index = %s"
    cursors.execute(sql, [index])
    data = cursors.fetchone()
    if not data:
        return False
    return True

def find_addr(table: str, index: str) -> str:
    """
    根据指定表内的指定索引寻找对应地址

    :param table: 待查索引所对应表
    :param index: 待查索引
    :return: 若存在返回索引对应地址，若不存在返回False
    """
    db_connection.ping(reconnect=True)
    cursors.execute(sql_index)
    db_connection.commit()
    sql = "SELECT address FROM %s" %table + " WHERE _index = %s"
    cursors.execute(sql, [index])
    data = cursors.fetchone()
    if not data:
        return False
    else:
        return data[0]
    

def add_index(table: str, index: str, addr: str) -> bool:
    """
    向指定表内增加指定索引以及相应的地址

    :param table: 待增加索引所对应表
    :param index: 待增加索引
    :param addr: 索引项对应地址
    :return: 若增加成功返回True，否则返回False
    """
    db_connection.ping(reconnect=True)
    cursors.execute(sql_index)
    db_connection.commit()
    if is_index_existing(table, index):
        return False
    try:
        sql = "INSERT INTO %s(_index, address)" %table + " VALUES(%s,%s)"
        cursors.execute(sql, [index, addr])
        db_connection.commit()
        return True
    except:
        return False
    
def del_index(table: str, index: str) -> bool:
    """
    删除指定表内的指定索引所在行

    :param table: 待删索引所对应表
    :param index: 待删索引
    :return: 若删除成功返回True，否则返回False
    """
    db_connection.ping(reconnect=True)
    cursors.execute(sql_index)
    db_connection.commit()
    if not is_index_existing(table, index):
        return False
    try:
        sql = "DELETE FROM %s" %table + " WHERE _index = %s"
        cursors.execute(sql, [index])
        db_connection.commit()
        return True
    except:
        return False
    
def modify_addr(table: str, index: str, addr: str) -> bool:
    """
    更改指定表内指定索引对应的地址

    :param table: 待改索引所对应表
    :param index: 待改索引
    :param addr: 索引项对应需要覆写的地址
    :return: 若修改成功返回True，否则返回False
    """
    db_connection.ping(reconnect=True)
    cursors.execute(sql_index)
    db_connection.commit()
    if not is_index_existing(table, index):
        return False
    try:
        sql = "UPDATE %s" %table + " SET address = %s WHERE _index = %s"
        cursors.execute(sql, [addr, index])
        db_connection.commit()
        return True
    except:
        return False