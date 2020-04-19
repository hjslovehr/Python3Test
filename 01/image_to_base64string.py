# -*- coding: utf-8 -*-

import base64

def image_to_base64string():
    while True:
        print('Please input file fullname: ')
        f = input()
        f = open(f, 'rb')
        b = f.read()
        b64Str = base64.b64encode(b)
        print(b64Str)
        print()

image_to_base64string()

    
# 用 input 阻塞程序退出
'''
print()
print('==================== Press "Enter" key to continue... ====================')
input()
'''
