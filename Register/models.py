from django.db import models

# Create your models here.
class Registeration(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    emailId=models.CharField(max_length=20)
    phonum=models.IntegerField()

    def __str__(self):
        return self.firstname

class Department(models.Model):
    deptname=models.CharField(max_length=20)
    registeration=models.ForeignKey(Registeration,on_delete=models.CASCADE,related_name='Department')