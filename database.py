# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:21:58 2020

@author: 11982
"""

import pymysql
import re


def insert1(top,moviename,director,writer,actors,type_film,date,timelong,IMDburl,introduction,movieurl):
    # print("coming")
    db = pymysql.connect("118.89.41.161",'doubanuser','douban123456','douban')
    print(db.encoding)
    cursor = db.cursor()
    # 简介出现双引号 无法直接插入数据表 需进行处理
    # 使用正则替换，便可以插入数据表中
    temp = re.compile("\"")
    text = temp.sub("\\\"", introduction)
    # SQL 插入语句
    sql1 = """INSERT INTO top VALUES ({}, "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""" \
    .format(top,moviename,director,writer,actors,type_film,date,timelong,IMDburl,introduction,movieurl)

    # SQL 查询语句
    sql2 = "select name from top where name='{}'".format(moviename)
    try:
        cursor.execute(sql2)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute(sql1)
            db.commit()
            print("Insert successfully.")
        else:
            print("The data existed")
    except:
        print("插入数据库失败")
        db.rollback()
    db.close()
    print("insert1")

def insert2(moviename,director,writer,actors,type_film,date,timelong,IMDburl,introduction,movieurl):
    db = pymysql.connect("118.89.41.161", "doubanuser", "douban123456", "douban")
    cursor = db.cursor()
    # 简介出现双引号 无法直接插入数据表 需进行处理
    # 使用正则替换，便可以插入数据表中
    temp = re.compile("\"")
    text = temp.sub("\\\"", introduction)
    # SQL 插入语句
    sql1 = """INSERT INTO movie VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""" \
        .format(moviename, director, writer, actors, type_film, date, timelong, IMDburl, introduction, movieurl)

    # SQL 查询语句
    sql2 = "select name from movie where name='{}'".format(moviename)
    try:
        cursor.execute(sql2)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute(sql1)
            db.commit()
            print("Insert successfully.")
        else:
            print("The data existed")
    except:
        print("插入数据库失败")
        db.rollback()
    db.close()
    print("insert2")

def select1(keyword):
    db = pymysql.connect("118.89.41.161", "doubanuser", "douban123456", "douban")
    cursor = db.cursor()

    sql = "select * from movie where name like '%{}%'".format(keyword)

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print("搜索结果有{}个".format(len(result)))

        index = 1
        for i in result:
            print("\nIndex:{}".format(index))
            print("豆瓣链接：{}".format(i[9]))
            print("片名：{}".format(i[0]))
            print("导演：{}".format(i[1]))
            print("编剧：{}".format(i[2]))
            print("主演：{}".format(i[3]))
            print("类型：{}".format(i[4]))
            print("上映日期：{}".format(i[5]))
            print("片长：{}".format(i[6]))
            print("IMDb：{}".format(i[7]))
            print("简介：\n{}".format(i[8]))

            index += 1
        print("select1")
    except:
        print("query error")
        db.rollback()
    db.close()
