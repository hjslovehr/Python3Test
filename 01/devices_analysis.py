import os
import json


# with open(r'C:\Users\DLAX\Desktop\宇视 LAPI Temp Files\channel-response.json', encoding='utf-8') as f:
#     json_str = f.read()

#     # 打印文件内容
#     # print(json_str)

#     obj = json.loads(json_str)
#     # print(obj)
#     print('StatusCode : {}'.format(obj['Response']['StatusCode']))

#     if 0 == obj['Response']['StatusCode']:
#         print('Request return OK!')
#         print('Array lenght: {}'.format(obj['Response']['Data']['Nums']))
#         # print(obj['Response']['Data']['DetailInfos'])
        
#         data = obj['Response']['Data']['DetailInfos']
#         # print(data)

#         for item in data:
#             if None != item.get('AddressInfo'):
#                 print('ID: {0}  Name: {1}  Address: {2}  Port: {3}  AccessAddress: {4}'.format(item['ID'], \
#                     item['Name'], \
#                     item['AddressInfo']['Address'], \
#                     item['AddressInfo']['Port'], \
#                     item['AddressInfo']['AccessAddress']))
#             else:
#                 print('ID: {0}  Name: {1} '.format(item['ID'], item['Name']))
                
#     else:
#         print('Request return Bad!')


obj = json.load(open(r'.\channel-response.json', encoding='utf-8'))
# print(json_str)
print('StatusCode : {}'.format(obj['Response']['StatusCode']))

if 0 == obj['Response']['StatusCode']:
    print('Request return OK!')
    print('Array lenght: {}'.format(obj['Response']['Data']['Nums']))
    # print(obj['Response']['Data']['DetailInfos'])
  
    data = obj['Response']['Data']['DetailInfos']
    # print(data)
    for item in data:
        if None != item.get('AddressInfo'):
            print('ID: {0}  Name: {1}  Status: {2}  Address: {3}  Port: {4}  AccessAddress: {5}'.format(item['ID'], \
                item['Name'], \
                item['Status'], \
                item['AddressInfo']['Address'], \
                item['AddressInfo']['Port'], \
                item['AddressInfo']['AccessAddress']))
        else:
            print('ID: {0}  Name: {1}  Status: {2} '.format(item['ID'], item['Name'], item['Status']))
          
else:
    print('Request return Bad!')

