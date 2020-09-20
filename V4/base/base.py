#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
# from V4.util.get_log import get_logging
from util.get_log import get_logging
import os


class Base():
    log = get_logging()

    # 初始化方法（实例化driver,调用我就给我传driver）
    def __init__(self):
        # self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://192.168.0.103:80/bugfree/index.php/site/login')
        self.log.info('打开bugfree网站！')

    # 查找元素
    def base_find_element(self, location, time_out=10, poll=0.5):
        # 设置默认超时时间为10秒,还可以指定超时时间和刷新频率
        # wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        wait = WebDriverWait(self.driver, timeout=time_out, poll_frequency=poll)
        # 获取元素
        # element = wait.until(ec.presence_of_element_located((By.ID, 'kw')))
        element = wait.until(ec.presence_of_element_located(location))
        # element = wait.until(lambda x: x.find_element(By.ID, 'kw'))
        # 返回元素，给其他方法使用
        self.log.info('获取到了页面元素！')
        return element

    # 点击方法
    def base_click(self, location):
        # 调用查找元素方法
        self.base_find_element(location).click()
        self.log.info('点击了元素！')

    # 输入方法
    def base_input(self, location, value):
        # 调用查询元素方法
        ele = self.base_find_element(location)
        self.log.info('获取到了input元素！')
        # 清空输入框
        ele.clear()
        self.log.info('清空了输入框！')
        # 输入内容
        ele.send_keys(value)
        self.log.info('输入内容！')

    # 获取文本方法
    def base_get_text(self, location):
        # 调用查找元素方法，获取页面异常提示信息，并返回
        return self.base_find_element(location).text
        self.log.info('获取到了页面异常提示信息！')

    # 截图方法
    def base_get_img(self):
        img_path = 'C://Users//Administrator//PycharmProjects//MyBugfree//V4//img//'
        self.driver.get_screenshot_as_file(img_path + '{}.png'.format(time.strftime('%Y-%m-%d_%H-%M-%S')))
        self.log.info('完成页面截图了！')

    # 断言方法
    def base_assert(self):
        pass
