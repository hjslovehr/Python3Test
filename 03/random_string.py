import random


def get_random_str(str_len:int):
    '''生成随机字符串'''
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    string_len = len(string)
    result = []
    for i in range(str_len):
        result.append(string[random.randint(0, string_len - 1)])
    return result


if __name__ == '__main__':
    str_len = int(input('请输入随机字符串长度: '))
    print(''.join(get_random_str(str_len)))


