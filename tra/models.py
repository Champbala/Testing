from django.db import models
from django.db.models.base import Model

# Create your models here.

class Destination(models.Model):

    dest_name=models.CharField(max_length=10)
    dest_price=models.IntegerField()
    dest_desc=models.CharField(max_length=20)
    dest_img=models.ImageField(upload_to='pics')
    dest_offer=models.BooleanField(default=False)

    def __str__(self):
        return self.dest_name  