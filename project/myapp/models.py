from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.CharField()
    image=models.ImageField(upload_to='image/')
    document=models.FileField(upload_to='file/') 
 