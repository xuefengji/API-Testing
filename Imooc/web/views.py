from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        return HttpResponse(user)
    else:
        return render(request,'login.html')