from django.shortcuts import render
from rest_framework.response import Response
from .models import Person
from . serializers import PersonSerializer
from rest_framework import status
from rest_framework import viewsets

class PersonViewSet(viewsets.ViewSet):
 def list(self,request):
  print("************List**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  pre= Person.objects.all()
  serializer = PersonSerializer(pre, many=True)
  return Response(serializer.data)

def retrieve(self, request, pk=None):
  print("************Retrieve**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  id = pk
  if id is not None:
    pre =Person.objects.get(id=id)
    serializer = PersonSerializer(pre)
    return Response (serializer.data)


def create(self, request):
  print("************Create**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  serializer = PersonSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


def update(self, request, pk):
  print("************Update**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  id = pk
  pre =Person.objects.get(pk=id)
  serializer = PersonSerializer(pre, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({'msg':'Data Updated'})
  return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


def partial_update(self, request, pk):
  print("************Partial_update**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  id = pk
  pre = Person.objects.get(pk=id)
  serializer = PersonSerializer(pre, data=request.data, partial=True)
  if serializer.is_valid():
    serializer.save()
    return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)



def destroy(self, request, pk):
  print("************Destroy**********")
  print("Basename:",self.basename)
  print("Action:",self.action)
  print("Detail:",self.detail)
  print("Syffix:",self.suffix)
  print("Name:",self.name)
  print("Description:",self.description)
  id =pk
  pre =Person.objects.get(pk=id)
  pre.delete()
  return Response ({'msg':"Data Deleted"})


  