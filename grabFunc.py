# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:51:27 2020

@author: 11982
"""

import requests
import random
import time
import database
from selenium import webdriver
from bs4 import BeautifulSoup

# 浏览器请求头
headerlist = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 Mobile/14B100 Safari/602.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0']
chrome_path = u'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

def rankList():
    print("rankList")
    i = 0
    while i < 10:
        grabPage(i)
        i += 1
        # don't forget to delete
        # return 1


def grabPage(pageNum):
    url = "https://movie.douban.com/top250?start={}&filter=".format(pageNum * 25)

    # 随机选择请求头
    header = dict()
    header["user-agent"] = random.choice(headerlist)
    # print(url)

    try:
        r = requests.get(url, headers=header)
        # print(url)
        r.raise_for_status()
        # print(r.encoding)
        # print(r.status_code)
        # xml = lxml.etree.HTML(r.text)
        # 获取类名为hd的div标签下的所有a标签的href属性  href装着电影链接url
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup)
        a = soup.select('.hd a')
        # print(a)

        i = 0
        count = pageNum * 25 + 1
        while i < (len(a)):
            print("TOP {}".format(count))
            # 遍历当前页面的所有电影链接
            flag = getMovieMessage(count, a[i].get('href'), 0)
            # print(a[i].get('href'))
            time.sleep(3)  # pause两秒 应付反爬
            if flag == 1:
                i += 1
                count += 1
                # print("+1")
            else:
                print("重新获取电影详细信息")
            # don't forget to delete
            # return 1

        return 1

    except:
        print("当前页无法访问！")
        return 0


def getMovieMessage(topNum, url, dbNum):
    print("getMovieMessage")
    print("豆瓣电影链接：{}".format(url))
    header = dict()
    header["user-agent"] = random.choice(headerlist)

    director = ''  # 导演
    writer = ''  # 编剧
    actors = ''  # 主演
    type_film = ''  # 类型
    date = ''  # 上映时间
    timelong = ''  # 时长
    IMDb = ''  # IMDb链接
    text = ''  # 简介
    video = ''  # 预告片

    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        #
        n = soup.select('#content h1 span')
        n_tag1 = n[0]
        n_tag2 = n[1]
        name = n_tag1.get_text() + n_tag2.get_text()
        print("片名：{}".format(name))

        info = soup.select('#info span .attrs')
        # print(info)
        for i in range(len(info)):
            if i == 0:
                x1 = info[0].select('a')
                for i in x1:
                    director += i.get_text() + " "
            elif i == 1:
                x2 = info[1].select('a')
                for i in x2:
                    writer += i.get_text() + " "
            elif i == 2:
                x3 = info[2].select('a')
                for i in x3:
                    actors += i.get_text() + " "

        print("导演：{}".format(director))
        print("编剧：{}".format(writer))
        print("主演：{}".format(actors))

        # 类型
        x4 = soup.select('span[property="v:genre"]')
        for i in x4:
            type_film += i.get_text() + " "
        print("类型：{}".format(type_film))

        # 日期
        x5 = soup.select('span[property="v:initialReleaseDate"]')
        for i in x5:
            date += i.get_text() + " "
        print("上映日期：{}".format(date))

        # 片长
        x6 = soup.select('span[property="v:runtime"]')
        for i in x6:
            timelong += i.get_text() + " "
        print("片长：{}".format(timelong))

        # 电影链接
        x7 = soup.select('div #info a')
        # print(x7)
        IMDb = x7[-1].get('href')
        print("IMDb链接：{}".format(IMDb))
        # 电影简介
        x8 = soup.select('span[property="v:summary"]')
        for i in range(len(x8)):
            text += "    " + x8[i].get_text().strip()
        print("简介：\n{}".format(text))

        if dbNum == 0:
            # 执行插入函数1;排行榜
            database.insert1(topNum, name, director, writer, actors, type_film, date, timelong, IMDb, text, url)
        elif dbNum == 1:
            # 执行插入函数2;列表
            database.insert2(name, director, writer, actors, type_film, date, timelong, IMDb, text, url)
        return 1

    except:
        print("无法访问电影详细信息")
        return 0


def latestList():
    drive = webdriver.Chrome(chrome_path)
    drive.get('https://movie.douban.com/')

    try:
        drive.implicitly_wait(3)
        a = drive.find_elements_by_xpath('//*[@id="screening"]/div[2]/ul/li/ul/li[1]/a')
        s = set()
        for i in a:
            s.add(i.get_attribute("href"))
        print("最新上映的电影有{}个".format(len(s)))
        l = list(s)

        for i in range(len(l)):
            print("序号：{}".format(i+1))
            getMovieMessage(i+1,l[i],1)
        print("newList")
    except:
        print("latest error")



def hotList():
    drive = webdriver.Chrome(chrome_path)  # 打开谷歌浏览器
    drive.get('https://movie.douban.com/')  # 打开一个网址
    try:
        # 等待3秒 浏览器加载javascript
        drive.implicitly_wait(3)
        # 通过xpath查找网页标签
        a = drive.find_elements_by_xpath('//*[@id="content"]/div/div[2]/div[4]/div[3]/div/div[1]/div/div//a')

        s = set()
        for i in a:
            s.add(i.get_attribute("href"))
        l = list(s)  # set转为list
        print("最近热门电影有{}个".format(len(l)))
        for i in range(len(l)):
            print("序号：{}".format(i + 1))
            # 获取电影详细信息
            getMovieMessage(0, l[i], 1)
            print("hotList")
    except:
        print("hotList error")



def search(name):

    drive = webdriver.Chrome(chrome_path)

    drive.get('https://movie.douban.com/subject_search?search_text={}&cat=1002'.format(name))
    try:
        a = drive.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/a')
        url = a.get_attribute('href')
        a.click()  # 点击连接
        # 获取电影详细信息
        getMovieMessage(0, url, 1)
        print("search")
    except:
        print(".....")




def queryBase():
    database.select1(input("input the keyword of the moviename:"))
    print("queryDatabase")
