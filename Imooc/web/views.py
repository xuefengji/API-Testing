from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
import json
import requests
# Create your views here.
#简单的登录接口
def Login(request):
    if request.method == 'POST':
        result = {}
        user = request.POST.get('username')
        password = request.POST.get('password')
        result['code'] = '200'
        result['cookie'] = user+':'+password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    if request.method == 'GET':
        result = {}
        user = request.GET.get('username')
        password = request.GET.get('password')
        result['user'] = user
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render(request,'login.html')

#获取user列表
def User(request):
    cookie = request.POST.get('cookie')
    result = {}
    if cookie:
        data = cookie.split(':')
        result['code'] = '200'
        result['mess'] = 'sucess'
        result['username'] = data[0]
        result['password'] = data[1]
    else:
        result['status_code'] = '500'
        result['mess'] = '没有权限'
    result = json.dumps(result,indent=2)
    return HttpResponse(result,content_type='application/json;charset=utf-8')
