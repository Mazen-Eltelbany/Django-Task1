from django.shortcuts import render
from django.http import HttpResponse
from .models import trainee
def alltraunees(request):
    context={}
    context['trainees']=trainee.objects.all()
    return render(request, 'trainee/list.html',context)
def updatetrainee(request,id):
    return HttpResponse(f"update trainee {id}")
def deletetrainee(request,id):
    return HttpResponse(f"delete trainee {id}")
def inserttrainee(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        image = request.FILES.get('image')

        t=trainee(name=name,email=email,image=image)
        t.save()
        return HttpResponse("Trainee inserted")
    return render(request,'trainee/insert.html')
def gettraineebyid(request,id):
    return HttpResponse(f"get trainee by id {id}")
