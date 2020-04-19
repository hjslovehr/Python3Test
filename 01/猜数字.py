import random

# 随机数
secret = random.randint(0, 9)
# 猜测次数
count = 0

while True:
    print('请输入一个（0~9之间）数字: ')
    s = input()
    count += 1
    if s == str(secret):
        print('猜对了，你真棒！')
        break
    else:
        print('太遗憾了，继续努力哦！')

print('猜测次数：' + str(count))
print('---------- 游戏结束 ----------')
