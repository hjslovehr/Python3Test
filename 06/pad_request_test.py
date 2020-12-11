import requests
import time


'''
url: 'http://192.168.0.112:8080/iclock/getrequest'
'''
def test(url:str):
    while True:
        try:
            r = requests.get(url)
            print(r.text)
        except Exception as ex:
            print(ex)
        
        time.sleep(1)
    pass


if __name__ == "__main__":
    test(input('请输入 URL: '))
