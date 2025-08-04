from django.http import HttpResponse

def hi(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("Welcome to Django")