import json
import os

def collection_analysis():
    while (True):
        file_path = input('请输入文件全名：')
        if not os.path.exists(file_path):
            print(f'{file_path} 不存在')
            continue

        json_str = ''
        with open(file_path, mode='r', encoding='utf-8') as f:
            json_str = f.read()
        
        json_object = json.loads(json_str)
        faceInfo = json_object['FaceInfoList'][0]
        cardInfo = json_object['CardInfoList'][0]
        
        person = {}
        person['Name'] = cardInfo['Name']
        person['Gender'] = cardInfo['Gender']
        person['Birthday'] = cardInfo['Birthday']
        person['CardID'] = cardInfo['CardID']
        person['ResidentialAddress'] = cardInfo['ResidentialAddress']
        person['IDImage'] = cardInfo['IDImage']
        person['IDImage'] = cardInfo['IDImage']['Data']
        person['FaceImage'] = faceInfo['FaceImage']['Data']

        print(json.dumps(person, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    collection_analysis()
    pass


