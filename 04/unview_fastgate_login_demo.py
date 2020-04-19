import requests
import json
import sys
sys.path.append('.\\common')
import md5_helper

def dict_display(data:dict):
    for key in data.keys():
        print(key, ':', data[key])
    pass

def login_test(url:str, user_name:str, pwd:str):
    print('原始数据:', user_name, pwd)
    pwd = md5_helper.get_md5_str(pwd)
    print('密码加密后:', pwd,)
    print()

    payload = {
        'id': user_name,
        'pwd': pwd
    }
    resp = requests.post(url=url, data=payload)
    resp.encoding = 'utf-8'
    # print(resp.headers)
    dict_display(resp.headers)
    print()
    print(resp.text)

    pass

if __name__ == '__main__':
    # login_test(input('请输入请求地址: '), input('请输入账号: '), input('请输入密码: '))
    login_test('https://www.baidu.com/', '123', '456')
    pass


