import requests

class OperationCookie:
    def get_cookie(self,method,url,data):
        if method == 'post':
            cookie = requests.post(url,data).cookies
        else:
            cookie = requests.get(url,data).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)
        return cookie

