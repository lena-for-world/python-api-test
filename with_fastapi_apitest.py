from fastapi import FastAPI
import json
import urllib.request
import secretKey

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello" : "root"}

@app.get("/api")
def read_api():
    key = secretKey.value
    urlTicker = urllib.request.urlopen("https://api.odcloud.kr/api/uws/v1/inventory?page=1&perPage=100&serviceKey="+key)
    readTicker = urlTicker.read()
    dict = json.loads(readTicker)
    for h in dict['data']:
        print(h['addr'])
