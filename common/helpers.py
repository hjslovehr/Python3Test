from datetime import datetime

# 函数用时装饰器
# 测试方法使用时间装饰器
def func_use_time(func):
    def use_time(*args, **kwargs):
        begin = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        sub = end - begin
        print(f'Total use time: {sub}')

    return use_time
