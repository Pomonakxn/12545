#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "强哥"


class ReadLocalElement():
    def read_data(self):
        file_path = '../config/localElement.ini'
        with open(file_path,'r',encoding='utf-8') as f:
            data = []
            for line in f.readlines():
                data.append(line.strip('\n').split('='))
        print(data)

if __name__ == '__main__':
    ReadLocalElement().read_data()
