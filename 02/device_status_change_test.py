import requests

data = '''
{
    "UpdateTime": "2020-02-26",
    "DeviceID": "B8C2C436-F722-426B-B619-70D7A48168EE",
    "StatusType": 1,
    "Status": 2,
    "Remarks": null
}
'''

header = { 'content-type' : 'application/json;charset=UTF-8' }

res = requests.post(url='http://localhost:46498/api/v10/Device/DeviceStateChange/', \
                    data=data, \
                    headers=header)

print(res.text)


