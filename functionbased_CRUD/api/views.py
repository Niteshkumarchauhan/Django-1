from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . serializers import PersonSerializer

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
 if request.method == 'GET':
     id = request.data.get('id')
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
      return Response({'MSG': 'DATA CREATED'})
  return Response(serializer.errors)
 if request.method == 'PUT':
    id = request.data.get('id')
    pre = Person.objects.get(pk=id)
    serializer = PersonSerializer(pre, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'MSG': 'DATA UPDATED'})
    return Response(serializer.errors)


 if request.method == 'DELETE':
    id = request.data.get('id')
    pre = Person.objects.get(pk=id)
    pre.delete()
    return Response({'MSG': 'DATA DELETED'})
  
    