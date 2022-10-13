from django.shortcuts import render
from rest_framework.response import Response
from .models import Person
from . serializers import PersonSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class StudentAPI(APIView):
  # GET
  def get(self, request,pk=None, formate=None):
     id = pk
     if id is not None:
         pre = Person.objects.get(id=id)
         serializer = PersonSerializer(pre)
         return Response(serializer.data)
     pre = Person.objects.all()
     serializer = PersonSerializer(pre, many=True)
     return Response(serializer.data)
  # POST
  def post(self, request, formate=None): 
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'DATA CREATED'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT
    
  def put(self, request,pk, formate=None): 
     id =pk
     pre = Person.objects.get(pk=id)
     serializer = PersonSerializer(pre, data=request.data)
     if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'Complete DATA UPDATED'})
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # PATCH
  def patch(self, request,pk, formate=None): 
    id =pk
    pre = Person.objects.get(pk=id)
    serializer = PersonSerializer(pre, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'Partial DATA UPDATED'})
    return Response(serializer.errors)
  
  # DELETE
  def delete(self, request,pk, formate=None): 
     id = pk
     pre = Person.objects.get(pk=id)
     pre.delete()
     return Response({'MSG': 'DATA DELETED'})
 
   

 
   
  
    