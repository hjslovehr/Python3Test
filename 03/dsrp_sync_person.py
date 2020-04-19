'''从 DSRP 同步人员'''

import json
import requests

def sync_person():
    '''同步人员'''
    pageIndex = 1
    pageSize = 10

    while True:
        print('发起第 {} 页请求'.format(pageIndex))
        result = get_persons(pageIndex, pageSize)
        if None == result:
            break
        
        # print(json.dumps(result, indent=4))
        # 将请求结果转为 DSRP 人员对象集合
        persons = convert_person(result)
        if None == persons or len(persons) == 0:
            break

        # 向 DFMS 添加人员
        success_count = dfms_add_person(persons)
        print('第 {} 页请求，总共 {} 条，成功 {} 条，失败 {} 条'\
            .format(pageIndex, len(persons), success_count, len(persons) - success_count))

        if 0 == success_count:
            break
        
        pageIndex = pageIndex + 1

    pass


def get_persons(pageIndex, pageSize):
    '''分页获取人员信息'''
    try:
        url = 'http://127.0.0.1:9011/ApiPersonInfo/GetPersonListInfo'
        data = f'{{"PageIndex": {pageIndex}, "PageSize": {pageSize}}}'
        headers = {}
        headers['Content-Type'] = 'application/json; charset=utf-8'
        resp = requests.post(url=url, data=data, headers=headers, timeout=10)
        resp.encoding = 'utf-8'
        # print('status', resp.status_code)
        # print(resp.text)
        jo = json.loads(resp.text)
        # print(json.dumps(jo, indent=4))
        return jo
    except Exception as e:
        print(e)
        return None
    pass


def convert_person(data:dict):
    '''将 data 转为 person 对象集合，并返回'''
    ls = data['data']
    # print(json.dumps(ls, indent=4))

    persons = []
    for item in ls:
        per = {}
        # 姓名
        per['PERSONNAME'] = item['Name']
        # 性别
        if None == item['Gender']:
            per['GENDER'] = None
        else:
            gender = int(item['Gender'])
            if 1 == gender:
                per['GENDER'] = 1
            elif 2 == gender:
                per['GENDER'] = 0
        # 身份证
        per['IDENTITYNO'] = item['IDCard']
        if None != per['IDENTITYNO'] \
            and len(str(per['IDENTITYNO']).strip()) != 0 \
            and len(str(per['IDENTITYNO']).strip()) > 50:
            per['IDENTITYNO'] = str(per['IDENTITYNO']).strip()[:50]
        # 电话
        per['PHONE'] = item['Phone']
        # 一卡通卡号
        per['ONECARDNO'] = item['OneCardNumber']
        # 照片
        per['PICLIST'] = []
        image = get_image(item['PhotoFileName'])
        if None != image:
            per['PICLIST'].append(image)

        print(json.dumps(per, indent=4))
        persons.append(per)

    return persons


def get_image(img_url:str):
    '''获取人员照片'''
    print('image url:', img_url)
    if None == img_url or len(img_url.strip()) == 0:
        return None

    file_name = img_url[img_url.replace('\\', '/').rfind('/') + 1:]
    print('File name:', file_name)
    
    try:
        resp = requests.get(img_url)
        print('status', resp.status_code)

        image = {}
        image['ContentType'] = 'image/jpeg'
        image['Name'] = 'file'
        image['FileName'] = file_name
        image['Data'] = resp.content

        return image
    except:
        pass

    return None


def dfms_add_person(persons:list):
    '''DFMS 新增人员'''
    if None == persons:
        return
    
    success_count = 0
    for item in persons:
        try:
            print(item)
            data = json.dumps(item)
            resp = requests.post(url='http://127.0.0.1:9001/V10/Person/Add', data=data, timeout=1)
            print(resp)
            success = success + 1
        except Exception as e:
            print(e)
        pass

    return success_count


if __name__ == "__main__":
    sync_person()
    pass


