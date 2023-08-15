import requests as rq

url = "http://192.168.0.102:8080"
data = {
    "name": "test2",
    "password": "xtremepc.axel4"
}

rq.post(url + "/store", json=data)
print(rq.get(url + "/get_users", json={"authentication":"xtremepc.axel3"}).content)