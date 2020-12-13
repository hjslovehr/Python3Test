class Student:
    # # 定义无参构造函数
    # def __init__(self):
    #     pass

    '''
    python 中构造函数不能重载
    '''
    # 定义构造函数
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    
    # 定义 __str__ 方法，会在 print() 中自动被调用
    def __str__(self):
        return 'Student [name: %s, age: %d]' % (self.__name, self.__age)


def main():
    stu = Student('king', 20)
    print(stu)


if __name__ == "__main__":
    main()
