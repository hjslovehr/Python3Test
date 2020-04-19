
import json
import requests


json_str = ''

payload = {
    'PageIndex': 1,
    'PageSize': 1000,
    'updateDateTime': "2020-01-01",
    'search_have_uersinfo': 1
}

data = json.dumps(payload)

headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

resp = requests.post(url='http://127.0.0.1:9011/ApiPersonInfo/GetPersonListInfo', data=data, headers=headers)

resp.encoding = 'utf-8'

json_str = resp.text

# print(json_str)

jo = json.loads(json_str)

data = jo['data']

print(len(data))

print(data)


