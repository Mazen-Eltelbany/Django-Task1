from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Trainee
from track.models import Track
def alltrainees(request):
    context={}
    context['trainees']=Trainee.getalltrainees().order_by('id')
    return render(request, 'trainee/list.html',context)
def updatetrainee(request,id):
    t=Trainee.getraineebyid(id)
    context={'trainee':t}
    context['tracks']=Track.getalltracks()
    if(request.method=='POST'):
        t.name=request.POST['name']
        t.email=request.POST['email']
        t.trackid=Track.gettrackbyid(request.POST['trtrack'])
        if request.FILES.get('image'):
            t.image = request.FILES['image']
        t.save()
        return redirect("alltrainees")
    return render(request, 'trainee/update.html', context)
def deletetrainee(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('alltrainees')
def inserttrainee(request):
    context={}
    context['tracks']=Track.getalltracks()
    if(request.method=='POST'):
        Trainee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            image=request.FILES['image'],
            trackid=Track.gettrackbyid(request.POST['trtrack'])
        )
        return redirect('alltrainees')
    return render(request, 'trainee/insert.html', context)

def gettraineebyid(request,id):
    return HttpResponse(f"get trainee by id {id}")
