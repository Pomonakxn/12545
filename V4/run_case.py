#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥@testrabbit.cn"


import unittest
import os
import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport


class RunCase():
    def test_case(self):
        case_path = os.path.join(os.getcwd() + '\\case\\')
        # print(case_path)
        # 批量执行测试用例-传入py文件的路径和模式（模糊匹配py文件）
        suite = unittest.defaultTestLoader.discover(case_path, 'test*.py')
        # 获取当前系统的时间
        current_time = time.strftime('%Y-%m-%d-%H_%M_%S')

        # 获取报告保存的路径
        report_name = os.path.join(os.getcwd() + '\\report\\' + 'report_' + current_time + '.html')
        # print(report_name)
        # 第一种：TXT测试报告
        # f = open(report_name, 'w')
        # runner = unittest.TextTestRunner(stream=f, verbosity=2)
        # runner.run(suite)
        # 第二种：HTML测试报告
        # f = open(report_name, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Bugfree自动化测试报告', description='登录功能-异常场景测试')
        # runner.run(suite)
        # f.close()
        # 第三种：BeautifulReport测试报告
        report_path = os.getcwd() + '\\report\\'
        report_name = 'report_' + current_time + '.html'
        print('路径是：', report_path)
        result = BeautifulReport(suite)
        result.report(description='登录功能-异常场景测试', filename=report_name, report_dir=report_path)


if __name__ == '__main__':
    RunCase().test_case()
