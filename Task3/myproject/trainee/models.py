from django.db import models
from track.models import Track
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    image=models.ImageField(upload_to='trainee/images')
    status=models.BooleanField(default=True)
    trackid = models.ForeignKey(Track, on_delete=models.CASCADE)

    @classmethod
    def getalltrainees(cls):
        return cls.objects.all()
    @classmethod
    def getraineebyid(cls,id):
        return cls.objects.get(id=id)
