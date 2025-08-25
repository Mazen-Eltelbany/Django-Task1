from django.db import models

class trainee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    image=models.ImageField(upload_to='trainee/images')
