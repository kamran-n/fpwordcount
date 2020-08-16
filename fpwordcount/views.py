from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def home(request):
    return HttpResponse('<h1>Salamlar</h1>')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist)})
