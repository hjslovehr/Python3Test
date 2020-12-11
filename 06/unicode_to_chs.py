
while (True):
    try:
        s = input('请输入内容(格式如：&#20154;&#33080;&#21517;&#21333;&#24211;): ')
        print(str.join('', [chr(int(it.replace('&#', ''))) for it in s.split(';') if it != '' and it != None]))
    except Exception as ex:
        print(ex)
