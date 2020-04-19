import json
import requests


def get_person_list_info():
    '''
    多条件查询人员信息接口
    '''
    payload = dict(PageIndex=1, PageSize=10)
    resp = requests.post('http://127.0.0.1:9011/ApiPersonInfo/GetPersonListInfo', data=payload)
    data = json.loads(resp.text)
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    get_person_list_info()


