from django.shortcuts import render
from django.http import HttpResponse
def alltracks(request):
    tracks=[[1,'Django'],[2,'Flask'],[3,'Dovops'],[4,'Python']]
    return render(request,'track/list.html',context={'tracks':tracks})
def gettrackbyid(request):
    return HttpResponse('<h1>Hello from id track</h1>')
def updatetrack(request,id):
    return HttpResponse(f'<h1>Hello from update track {id}</h1>')

def inserttrack(request):
    return render(request,'track/insert.html')

def deletetrack(request,id):
    return HttpResponse(f'<h1>track {id} deleted</h1>')