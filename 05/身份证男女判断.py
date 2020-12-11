
def get_gender_by_idnum():
    while (True):
        idnum = input('请输入身份证号(15位或者18位): ')
        num_len = len(idnum)
        if 15 != num_len and num_len != 18:
            print('身份证号长度不对')
            continue
        
        if 15 == num_len:
            if int(idnum[num_len - 1]) & 1 == 1:
                print(idnum, ':', '男')
            else:
                print(idnum, ':', '女')
        else:
            if int(idnum[num_len - 1 - 1]) & 1 == 1:
                print(idnum, ':', '男')
            else:
                print(idnum, ':', '女')

        pass

if __name__ == "__main__":
    get_gender_by_idnum()
    pass

