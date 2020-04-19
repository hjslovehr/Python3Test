# 导入 time 模块
import time

localTime = time.localtime()
timeStr = time.strftime('%Y-%m-%d %H:%M:%S', localTime)
t = time.strptime(timeStr, '%Y-%m-%d %H:%M:%S')

print(timeStr + ' ==> ' + str(int(time.mktime(t))))

# 用 input 阻塞程序退出
print()
print('==================== Press "Enter" key to continue... ====================')
input()
