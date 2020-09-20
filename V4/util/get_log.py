#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"


import logging
import time
import os

def get_logging():
    # 设置日志的输出格式：日志级别 时间  [logger的名字] [模块名_函数名:行数] - 输出信息
    fmt = '%(levelname)s %(asctime)s [%(name)s]  [%(filename)s %(funcName)s:%(lineno)d] - %(message)s'
    # fmt = '%(asctime)s %(levelname)s [%(name)s]  [%(filename)s %(funcName)s:%(lineno)d] - %(message)s'

    # 设置日志保存到指定文件中
    log_path = 'C://Users//DELL//PycharmProjects//My20200920//V4//log//'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename=log_path+'{}.log'.format(time.strftime('%Y-%m-%d')))

    # 调用指定日志级别，输出日志信息
    # logging.debug('这是debug信息')
    return logging
