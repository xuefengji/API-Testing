import requests


def send_post(url,data):
    res = requests.post(url,data)
    return res.json()
def send_get(url,data):
    res = requests.get(url,data)
    return res.json()
def run(url,data,method):
    res = None
    if method == 'POST':
        res = send_post(url,data)
    if method == 'GET':
        res = send_get(url,data)
    return res

if __name__=='__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {'username': 'dddddd', 'password': 11111111}
    res = run(url,data,"POST")
    print(res)