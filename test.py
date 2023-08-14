import requests as rq

url = "http://192.168.0.104:8080/store"
data = {
    "name": "test",
    "password": "xtremepc.axel3"
}

rq.post(url, json=data)