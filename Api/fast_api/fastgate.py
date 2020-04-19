from fastapi import FastAPI, Response
import json

app = FastAPI()

@app.get('/fastgate/')
def index():
    return 'index'

@app.post('/fastgate/user/login/')
def login(data:dict):
    print('data', ':', data)
    resp = Response()
    resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
    resp.headers['Set-Cookie'] = 'JSESSIONID=8BC8CCFB02A517C887C83B1DE9F4AE17; Path=/fastgate; HttpOnly'
    login_result = ''
    with open('.\\fastgate_login.json', 'r', encoding='utf-8') as f:
        login_result = f.read()
    resp.body = bytes(login_result, encoding='utf-8')
    return resp

@app.get('/fastgate/departments/')
def departments(conditionParam:str):
    print('conditionParam', ':', conditionParam)
    dpts = ''
    with open('.\\departments.json', 'r', encoding='utf-8') as f:
        dpts = f.read()
    return json.loads(dpts)

@app.get('/fastgate/areas/')
def areas(conditionParam:str):
    print('conditionParam', ':', conditionParam)
    dpts = ''
    with open('.\\departments.json', 'r', encoding='utf-8') as f:
        dpts = f.read()
    return json.loads(dpts)
