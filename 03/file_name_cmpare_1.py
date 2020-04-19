import os
import shutil

def file_name_compare(file_path:str):
    file_names = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            print(os.path.join(root, file), '==>', os.path.join(root, file.split('_')[-2] + '.jpg'))
            os.rename(os.path.join(root, file), os.path.join(root, file.split('_')[-2] + '.jpg'))

    pass


if __name__ == "__main__":
    file_name_compare(input('请输入文件夹绝对路径: '))
    pass


