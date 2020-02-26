# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 1:48
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_sina.py
# @Software: PyCharm

from page.sina import *
from page.init import *

class SinaTest(InitWeb,Sina):

    def test_sinaLogin_001(self,parent='divText',value='emailNull'):
        '''登录业务：账号密码为空验证'''
        self.login('','')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

    def test_sinaLogin_002(self,parent='divText',value='emailFormat'):
        '''登录业务：输入不规范邮箱名'''
        self.login('dengbanghan','han920929')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

if __name__ == '__main__':
    unittest.main(verbosity=2)