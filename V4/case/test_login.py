#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"


# 导包
import unittest
import ddt
# from V4.page.page_login import PageLogin
from page.page_login import PageLogin
# from V4.util.read_excel_file import ReadExcelFile
from util.read_excel_file import ReadExcelFile


# 新建测试类
@ddt.ddt()
class TestLogin(unittest.TestCase):
    # 初始化方法
    @classmethod
    def setUpClass(self):
        # 实例化，获取PageLogin()对象
        self.login = PageLogin()

    # 结束方法
    @classmethod
    def tearDownClass(self):
        self.login.driver.quit()

    @ddt.data(*ReadExcelFile().get_excel_data())
    @ddt.unpack
    def test_login(self, username, password, result):
        # 调用登录方法
        self.login.page_login(username, password)
        # 断言
        tip = self.login.page_get_text()
        self.login.log.info(tip)
        self.login.log.info(result)
        self.assertEqual(tip,result )
        # try:
        #     tip = self.login.page_get_text()
        #     self.login.log.info(tip)
        #     self.login.log.info(result)
        #     # self.assertEqual(tip, result)
        #     assert tip == result
        # except AssertionError:
        #     # 截图
        #     self.login.page_get_img()


if __name__ == '__main__':
    unittest.main()
