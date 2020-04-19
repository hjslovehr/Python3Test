import json
import os
import base64
import uuid

def analysis_person_event_info(filename:str):
    print("filename: {}".format(filename))
    if (not os.path.exists(filename)):
        print('File {} not exists'.format(filename))
        return

    obj = json.load(open(filename, encoding='utf-8'))
    person_event_info = obj['PersonEventInfo']
    # 打印信息
    print('ID: {}'.format(person_event_info['ID']))
    print('Timestamp: {}'.format(person_event_info['Timestamp']))
    print('NotificationType: {}'.format(person_event_info['NotificationType']))
    print('FaceInfoNum: {}'.format(person_event_info['FaceInfoNum']))

    # FaceInfoList
    face_info_list = person_event_info['FaceInfoList'][0]
    print('FaceInfoList:')
    white_space = str(1 * '\t')
    print('{}Type: {}'.format(white_space, face_info_list['Type']))
    print('{}PassingTime: {}'.format(white_space, face_info_list['PassingTime']))
    print('{}ChannelID: {}'.format(white_space, face_info_list['ChannelID']))

    # CompareInfo
    compare_info = face_info_list['CompareInfo']
    person_info = compare_info['PersonInfo']
    print(f'{white_space}CompareInfo:')
    white_space = str(2 * '\t')
    print(f'{white_space}Similarity: {compare_info["Similarity"]}')
    print(f'{white_space}PersonInfo:')
    white_space = str(3 * '\t')
    print('{}PersonID: {}'.format(white_space, person_info['PersonID']))
    print('{}PersonName: {}'.format(white_space, person_info['PersonName']))

    # SnapshotImage
    snapshot_image = compare_info['SnapshotImage']
    white_space = str(2 * '\t')
    print(f'{white_space}SnapshotImage:')
    white_space = str(3 * '\t')
    # SmallImage
    small_image = snapshot_image['SmallImage']
    print(f'{white_space}SmallImage:')
    white_space = str(4 * '\t')
    print('{}Size: {}'.format(white_space, small_image['Size']))

    save_file(small_image['Data'])

    pass # end of analysis_json


def save_file(base64string):
    file_name = f'c:/users/dlax/desktop/{uuid.uuid4()}.jpg'
    with open(file_name, mode='wb+') as f:
        f.write(base64.b64decode(base64string))
    
    print(f'Save file : {file_name}')

    pass # end of save_file


file_name = input("请输入 Json 文件名称：");
analysis_person_event_info(file_name)


