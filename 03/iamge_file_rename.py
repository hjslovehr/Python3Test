'''批量图片重命名'''

import os
import shutil
import datetime

def image_rename():
    path = input('请输入文件夹路径：')
    print(path)

    print(datetime.datetime.now())
    print(('=' * 20) + ' 开始 ' + ('=' * 20))
    print('操作进行中...')

    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            result_path = os.path.join(path, 'result')
            if not os.path.exists(result_path):
                os.mkdir(result_path)
            
            print('创建 result 文件夹')
            print('文件拷贝并重命名操作进行中...')

            with open(os.path.join(path, 'change_result.txt'), 'w', encoding='utf-8') as f:
                for file in files:
                    file_name = file.split('_')
                    new_filename = os.path.join(path, 'result', file_name[1] + '.jpg')
                    # print(file, ' ==> ', new_filename)
                    # 拷贝文件
                    shutil.copyfile(os.path.join(path, file), new_filename)
                    # 打印结果，并保存到文本文件中
                    f.write(file + '  => ' + new_filename + '\r\n')
    
    print(('=' * 20) + ' 结束 ' + ('=' * 20))
    print(datetime.datetime.now())
    pass


if __name__ == "__main__":
    image_rename()
    pass

