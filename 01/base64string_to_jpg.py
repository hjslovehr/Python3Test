# -*- coding:utf-8 -*-

import time
import base64
import os

def get_file_name():
    return os.getcwd() + "\\" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())

def base64string_to_jpg():
    while True:
        try:
            print('Plase input file fullname: ')
            fileName = input()
            file = open(fileName)
            base64str = file.read()
            file.close()

            # base64string 转 bye 数组
            imageData = base64.b64decode(base64str)
            
            fileName = get_file_name() + '.jpg'
            file = open(fileName, 'wb')
            file.write(imageData)
            file.close()
        
            print(fileName + " saved ! ");
        except OSError as err:
            print(err)

base64string_to_jpg()


# 用 input 阻塞程序退出
'''
print()
print('==================== Press "Enter" key to continue... ====================')
input()
'''
