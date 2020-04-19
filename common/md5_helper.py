import hashlib

def get_md5_str(src:str):
    '''生成 MD5 字符串'''
    md5 = hashlib.md5()
    md5.update(src.encode('utf-8'))
    return md5.hexdigest()
