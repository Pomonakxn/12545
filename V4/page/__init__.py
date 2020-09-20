#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"

# 登录页面元素信息
from selenium.webdriver.common.by import By

# 用户名
login_username = (By.ID, 'LoginForm_username')
# 密码
login_password = (By.ID, 'LoginForm_password')
# 登录按钮
login_button = (By.ID, 'SubmitLoginBTN')
# 页面提出提示信息
login_tip = (By.ID, 'login-error-div')
