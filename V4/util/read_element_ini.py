#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥@testrabbit.cn"

import configparser


class ReadIni():
    # 初始化ReadIni对象的变量，file_name是配置文件的路径，node是配置文件中的节点
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = '../config/element.ini'
        if node is None:
            self.node = 'LoginElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载配置文件
    def load_ini(self, file_name):
        # 实例化configparser类的对象
        cf = configparser.ConfigParser()
        # 获取配置文件的路径
        print('配置文件的路径是：' + file_name)
        # 读取配置文件
        cf.read(file_name)
        return cf

    # 获取关键字的值，key是节点中的关键字
    def getValue(self, key):
        # 打印配置文件中LoginElement节点中username的值
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.getValue('username'))
