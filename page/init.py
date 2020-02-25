# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:35
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : init.py
# @Software: PyCharm

import unittest
from utils.operationXml import *
from selenium import webdriver

class InitWeb(unittest.TestCase,OperationXml):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')

    def tearDown(self):
        self.driver.quit()