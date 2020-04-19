import json
import os

def get_all_department(file_name:str):
    json_str = ''
    with open(file_name, mode='r', encoding='utf-8') as f:
        json_str = f.read()
    # print(json_str)

    dpts = json.loads(json_str, encoding='utf-8')['data']
    # print(dpts)

    # for item in dpts:
    #     # print(item)
    #     print(item['Name'], ',', item['Code'], ',', item['Parentcode'])
    #     pass

    print('=' * 60)

    result = []
    parent = [it for it in dpts if it['Code'] == 'iccsid'][0]
    parent['Space'] = ''
    org_list_to_json(dpts, parent, result, '────')

    # print(json.dumps(result, indent=4, ensure_ascii=False))

    show_org_json(result)

    pass


def org_list_to_json(data:list, parent:dict, result:list, space:str):
    result.append(parent)
    parent['Children'] = []
    for item in data:
        if item['Parentcode'] == parent['Code'] and item['Code'] != parent['Code']:
            white_space = ''
            if None != parent['Space'] and len(parent['Space']) > 0:
                white_space = ' ' * len(parent['Space'])
            item['Space'] = white_space + '└' + space
            parent['Children'].append(item)

            # 判断 item 是否存在下级
            temp = [it for it in data if it['Parentcode'] == item['Code'] and it['Code'] != item['Code']]
            if None != temp and len(temp) > 0:
                item['Children'] = []
                org_list_to_json(data, item, item['Children'], space)
    pass


def show_org_json(data:list):
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    # print(data)
    for item in data:
        print(item['Space'], item['Name'], ',', item['Code'], ',', item['Parentcode'])
        Children = item.get('Children')
        if None != Children:
            show_org_json(Children)
        pass
    pass


if __name__ == "__main__":
    get_all_department('.\\04\\departments.json')


