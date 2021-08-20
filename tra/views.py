from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    dest=Destination.objects.all()
    # dest.dest_price=100
    # dest.dest_desc="welcome"
    # dest.dest_img='destination_1.jpg'
    # dest.dest_offer=True

    # dest1=Destination()
    # dest1.dest_price=100
    # dest1.dest_desc="welcome"
    # dest1.dest_img='destination_2.jpg'
    # dest1.dest_offer=True

    # des=[dest,dest1]


    return render(request, 'index.html',{'dest':dest})
