import http
from django.shortcuts import render
from django.http import HttpResponse
# from pytube import YouTube
# Create your views here.
def index(request):
    return HttpResponse('Index Page!')

def web(request):
    return render(request,'gapp/index.html')

def git(request):
    return HttpResponse('This is a GIT page!')


def home(request):
    return render(request, 'gapp/home.html')