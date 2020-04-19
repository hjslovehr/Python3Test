import os
import shutil

def file_name_compare(file_path:str, txt_file:str, result_file_name:str):
    file_names = []
    for root, dirs, files in os.walk(file_path):
        for f in files:
            file_names.append(f.split('_')[-2] + '.jpg')
    # print(file_names)

    lines = []
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # print(lines)

    names = []
    dd = {}
    for item in lines:
        names.append(item.split('\\')[-1].replace('\n', ''))
        dd[item.split('\\')[-1].replace('\n', '')] = item
    # print(names)

    count = 0
    with open(result_file_name, 'w', encoding='utf-8') as f:
        for name in names:
            if name in file_names:
                continue;
            else:
                print(name, ' is not image file')
                f.write(dd[name])
                count = count + 1
        
    print('not file', count, '个文件')

    pass


if __name__ == "__main__":
    file_name_compare(input('请输入照片路径:'), input('请输入文件全名:'), input('请输入比对结果文件全名:'))
    pass


