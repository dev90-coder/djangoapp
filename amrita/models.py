from django.db import models

# Create your models here.
class student(models.Model):
    phone = models.CharField(max_length=1000)
    father = models.CharField(max_length=1000)
    mother = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='static',default='h')
    student = models.CharField(max_length=1000)
    cls = models.CharField(max_length=2,default="-")
    dob = models.DateField(default='2024-10-09')
    addmission = models.CharField(max_length=1000)
    def __str__(self):  
        return self.student
class cont(models.Model):
    name =  models.CharField(max_length=1000)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=500)
    def __str__(self):
        return self.name
class suggests(models.Model):
    mem =  models.CharField(max_length=1000)
    
    desig = models.CharField(max_length=1000)
    text= models.TextField(max_length=500)
    sug_f = models.CharField(max_length=100)
    emails = models.EmailField(max_length=100)
    classes = models.CharField(max_length=1000)
    def __str__(self):
        return self.mem