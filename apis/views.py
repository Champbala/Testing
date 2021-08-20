from django.shortcuts import render

# Create your views here.
from .serializers import StudSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudSerializer
# Create your views here.


@api_view(['GET'])
def viewdetails(request):
    Reg=Student.objects.all()
    Regser=StudSerializer(Reg,many=True)
    return Response(Regser.data)

@api_view(['GET'])
def viewiddetails(request,pk):
    Reg=Student.objects.get(id=pk)
    Regser=StudSerializer(Reg,many=False)
    return Response(Regser.data)

@api_view(['POST'])
def Updatedetails(request):
    Regser=StudSerializer(data=request.data)
    if Regser.is_valid():
        Regser.save()
    return Response(Regser.data)

@api_view(['POST'])
def Updatedetailsid(request,pk):
    Reg=Student.objects.get(id=pk)
    Regser=StudSerializer(instance=Reg ,data=request.data)
    if Regser.is_valid():
        Regser.save()
    return Response(Regser.data)

@api_view(['DELETE'])
def delete(request,pk):
    Reg=Student.objects.get(id=pk)
    Reg.delete()
    return Response('deleted')

