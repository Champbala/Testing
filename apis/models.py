from abc import abstractmethod
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=10)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    dept=models.CharField(max_length=10)
    joindate=models.DateTimeField()
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self) -> str:
        return self.name


class college(models.Model):
    clgname=models.CharField(max_length=20)
    deptname=models.CharField(max_length=20)
    place=models.CharField(max_length=20)

    class Meta:
        abstract=True

 
  
  
class Proffessor(college):  # TEACHER
    name = models.CharField(max_length=100)
    ID = models.IntegerField()

    def __str__(self) -> str:
        return self.name