from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Person
from . serializers import PersonSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
 if request.method == 'GET':
     id = pk
     if id is not None:
         pre = Person.objects.get(id=id)
         serializer = PersonSerializer(pre)
         return Response(serializer.data)
     pre = Person.objects.all()
     serializer = PersonSerializer(pre, many=True)
     return Response(serializer.data)
 if request.method == 'POST':
  serializer = PersonSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'DATA CREATED'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 if request.method == 'PUT':
    id =pk
    pre = Person.objects.get(pk=id)
    serializer = PersonSerializer(pre, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'Complete DATA UPDATED'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 if request.method == 'PATCH':
    id =pk
    pre = Person.objects.get(pk=id)
    serializer = PersonSerializer(pre, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'Partial DATA UPDATED'})
    return Response(serializer.errors)


 if request.method == 'DELETE':
    id = pk
    pre = Person.objects.get(pk=id)
    pre.delete()
    return Response({'MSG': 'DATA DELETED'})
  
    