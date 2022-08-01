from django.shortcuts import render
from django.http import HttpResponse

from . import forms
from .models import profile
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
     return render(request, 'index.html')



def login_request(request):
    if request.method=='GET':
        return render(request,'login.html')
    
# def dashboard(request):
    if request.method=='POST':
        # breakpoint()
        full_name = request.POST['full_name']
        password = request.POST['password']
        user = profile.objects.get(full_name=full_name, password=password)
        
        if user is not None:
            # message = f'Hello {user.full_name}! You have been logged in'
            # return redirect('document.html')
            return render(request,'dashboard.html')
        else:
            # message = 'Login failed!'
            return HttpResponse('user or password invalid!')
