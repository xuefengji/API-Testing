from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
import json
import requests
# Create your views here.


def Login(request):
    if request.method == 'POST':
        result = {}
        user = request.POST.get('username')
        password = request.POST.get('password')
        result['user'] = user
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render(request,'login.html')