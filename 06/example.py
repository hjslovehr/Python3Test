from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    key: str = None

app = FastAPI()

@app.get('/')
def get():
    return 'get test'


@app.post('/')
def post(params: Item):
    print(params)
    return f'post data: {params}' 


if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=8088, log_level="info")
    pass


