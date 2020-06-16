# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:47:58 2020

@author: 11982
"""

import myFilm_menu
import time



while True:
    flag = myFilm_menu.menu()
    if flag == 0 :
        break
    time.sleep(1)