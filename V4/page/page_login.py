#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"

# 导包

# from V4.base.base import Base
from base.base import Base
# 调用_init_.py
# from V4 import page
import page
# from V4.util import get_log
from util import get_log

class PageLogin(Base):  # 继承Base类
    # 输入用户名
    def page_input_username(self, username):
        # self.driver.find_element_by_id('LoginForm_username').clear()
        # self.driver.find_element_by_id('LoginForm_username').send_keys(username)
        self.base_input(page.login_username, username)
        self.log.info('输入用户名了！')

    # 输入密码
    def page_input_password(self, password):
        # self.driver.find_element_by_id('LoginForm_password').clear()
        # self.driver.find_element_by_id('LoginForm_password').send_keys(password)
        self.base_input(page.login_password, password)
        self.log.info('输入密码了！')

    # 点击登录按钮
    def page_click_btn(self):
        # self.driver.find_element_by_id('SubmitLoginBTN').click()
        self.base_click(page.login_button)
        self.log.info('点击按钮了！')

    # 获取页面异常提示信息
    def page_get_text(self):
        # tip = self.driver.find_element_by_id('login-error-div').text
        # return tip
        return self.base_get_text(page.login_tip)

    # 截图
    def page_get_img(self):
        self.base_get_img()

    # 业务层，组装方法
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_btn()
        self.page_get_text()
