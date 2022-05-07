from ctypes.wintypes import HACCEL
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
          {
             'author': 'JK',
             'title':  'HP'
          } ,

          {
             'author': 'WS',
             'title':  'JC'
          }
]

def home(request):
    content = { 'posts' : posts ,
                'title' : 'AUTHORS'        }
    return render(request,'blog/home.html' , content )

def about(request):
    return render(request, 'blog/about.html')