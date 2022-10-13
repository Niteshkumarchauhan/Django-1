# from functools import partial
# from django import dispatch
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name= 'dispatch')

class PersonAPI(View):
   def get(self, request, *args, **kwargs ):
     json_data = request.body
     stream = io.BytesIO(json_data)
     pythondata = JSONParser().parse(stream)
     id = pythondata.get('id', None)
     if id is not None:
        #  print("AAAA",id,  Person.objects.get(id = 3))
      pre = Person.objects.get(id = id)
      Serializer = PersonSerializer(pre)
      json_data = JSONRenderer().render(Serializer.data)
      return HttpResponse(json_data, content_type='application/json')

     pre = Person.objects.all()
     Serializer = PersonSerializer(pre, many=True)
     json_data = JSONRenderer().render(Serializer.data)
     return HttpResponse(json_data, content_type='application/json')



   def post(self, request, *args, **kwargs ):
     json_data = request.body
     stream = io.BytesIO(json_data)
     pythondata = JSONParser().parse(stream)
     serializer = PersonSerializer(data=pythondata)
     if serializer.is_valid():
        # pdb.set_trace()
      serializer.save()
      res = {'msg': 'Data Created'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
     json_data = JSONRenderer().render(serializer.errors)
     return HttpResponse(json_data, content_type='application/json')




   def put(self, request, *args, **kwargs ):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    pre = Person.objects.get(id=id)
    serializer = PersonSerializer(pre, data=pythondata,
    partial=True)
    if serializer.is_valid():
        # pdb.set_trace()
     serializer.save()
     res = {'msg': 'Data Updated'}
     json_data = JSONRenderer().render(res)
     return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')






   def delete(self, request, *args, **kwargs ):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    pre = Person.objects.get(id=id)
    pre.delete()
    res = {'msg': 'Data Deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')  


               


