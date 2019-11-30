import requests


url = 'http://127.0.0.1:8000/login/'

data = {'username':'dddddd','password':11111111}

res = requests.get(url,params=data)
print(res.json())