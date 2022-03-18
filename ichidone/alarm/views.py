from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, "alarm/index.html", data)

def login(request):
    return render(request,)
    
def logout(request):
    return render(request,)