from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Track
def alltracks(request):
    context={}
    context['tracks']=Track.objects.filter(status=True)
    return render(request,'track/list.html',context)
def gettrackbyid(request):
    return HttpResponse('<h1>Hello from id track</h1>')
def updatetrack(request,id):
    if(request.method=='POST'):
        name=request.POST['name']
        t=Track(id=id,name=name)
        t.save()
        return HttpResponseRedirect('/track/')
    return HttpResponse(f'<h1>Hello from update track {id}</h1>')

def inserttrack(request):
    if(request.method=='POST'):
        name=request.POST['name']
        t=Track(name=name)
        t.save()
        return HttpResponseRedirect('/track/')
    return render(request,'track/insert.html')

def deletetrack(request,id):
    Track.objects.filter(id=id).update(status=False)
    return redirect('alltracks')