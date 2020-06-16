# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:47:07 2020

@author: 11982
"""
import grabFunc

def menu():
    print("""MENU: 
         
        1 TOP250
        2 NEW
        3 HOT
        4 SEARCH
        5 QUERY DATABASE
        0 EXIT
          """)
    op = int( input("Input a number between 0 and 5:\n") )
    if op < 0 and op >5:
        print("Bad request.Try again.")
        return 1
    if op == 0 :
        return 0
    if op == 1 :
        grabFunc.rankList()
    if op == 2 :
        grabFunc.latestList()
    if op == 3 :
        grabFunc.hotList()
    if op == 4 :
        name = input("input keyword:")
        grabFunc.search(name)
    if op == 5 :
        grabFunc.queryBase()
    