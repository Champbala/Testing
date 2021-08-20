from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Vechicle(models.Model):
    name=models.CharField(max_length=10)
    #OnetoOne Relationship
    Customer=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Vechicle')
   

    def __str__(self) -> str:
        return self.name
