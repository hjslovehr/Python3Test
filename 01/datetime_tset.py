import time
import datetime

dt = time.localtime()

print(time.strftime('%Y-%m-%d %H:%M:%S', dt))

print(datetime.datetime.now())

# 用 input 阻塞程序退出
print()
print('==================== Press "Enter" key to continue... ====================')
input()
