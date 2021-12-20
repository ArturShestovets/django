from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    return render(request, 'main/blog.html')

def login(request):
    return render(request, 'main/login.html')

def catalogue(request):
    return render(request, 'main/login.html')