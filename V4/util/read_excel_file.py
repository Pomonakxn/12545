#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥@testrabbit.cn"


# 导入操作excel的第三方库
import xlrd


class ReadExcelFile(object):
    # 初始化两个变量，excelPath为excel文件的保存路径，sheetName为sheet表的名称
    def __init__(self, excelPath=None, sheetName="Sheet1"):
        if excelPath is None:
            excelPath = r'C:\Users\DELL\PycharmProjects\My20200920\V4\data\login_data.xls'
        # 打开该excelPath路径下的excel文件
        self.data = xlrd.open_workbook(excelPath)
        # 通过excel中sheet名称读取该sheet表中的数据
        self.table = self.data.sheet_by_name(sheetName)
        # 也可以通过excel中sheet索引读取该sheet表中的数据
        # self.data.sheet_by_index(0)
        # 读取总行数
        self.rowNum = self.table.nrows
        # 读取总列数
        self.colNum = self.table.ncols

    def get_excel_data(self):
        # 定义一个空的列表来存放excel中的数据，格式是：[[],[],[]]
        row_data = []
        # 循环获取excel中的行
        for n in range(self.rowNum):
            row = self.table.row_values(n)
            # 将获取的行的数据添加到列表中
            row_data.append(row)
        # 返回该列表的数据
        return row_data


if __name__ == "__main__":
    print(ReadExcelFile().get_excel_data())

