from django.shortcuts import render
from django.http import HttpResponse
def alltraunees(request):
    li=[[1,'Ahmed','010'],[2,'Ali','011'],[3,'Mohamed','012']]
    return render(request, 'trainee/list.html',context={'trainees':li})
def updatetrainee(request,id):
    return HttpResponse(f"update trainee {id}")
def deletetrainee(request,id):
    return HttpResponse(f"delete trainee {id}")
def addtrainee(request):
    return HttpResponse("add trainee")
def gettraineebyid(request,id):
    return HttpResponse(f"get trainee by id {id}")
