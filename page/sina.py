# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:47
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : sina.py
# @Software: PyCharm

from base.basePage import *
from selenium.webdriver.common.by import By

class Sina(WebDriver):
    username_loc=(By.ID,'freename')
    password_loc=(By.ID,'freepassword')
    login_loc=(By.LINK_TEXT,'登录')
    loginError_loc=(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')

    def typeUserName(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getLoginError(self):
        '''获取错误的信息'''
        return self.findElement(*self.loginError_loc).text