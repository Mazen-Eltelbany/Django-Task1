from django.db import models
class Track(models.Model):
    name=models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    @classmethod 
    def getalltracks(cls):
        return cls.objects.all()
    @classmethod
    def gettrackbyid(cls,id):
        return cls.objects.get(id=id)

