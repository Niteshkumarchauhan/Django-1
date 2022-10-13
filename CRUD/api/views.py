from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt      


# import pdb
def person_api(request):

    # GET method
    # if request.method == 'GET':
    #     # pdb.set_trace()
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id', None)
    #     if id is not None:
    #     #  print("AAAA",id,  Person.objects.get(id = 3))
    #      pre = Person.objects.get(id = id)
    #      Serializer = PersonSerializer(pre)
    #      json_data = JSONRenderer().render(Serializer.data)
    #      return HttpResponse(json_data, content_type='application/json')

    # pre = Person.objects.all()
    # Serializer = PersonSerializer(pre, many=True)
    # json_data = JSONRenderer().render(Serializer.data)
    # return HttpResponse(json_data, content_type='application/json')


    # POST method

    # if request.method == 'POST':
    #     # pdb.set_trace()
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializer = PersonSerializer(data=pythondata)
    # if serializer.is_valid():
    #     # pdb.set_trace()
    #     serializer.save()
    #     res = {'msg': 'Data Created'}
    #     json_data = JSONRenderer().render(res)
    #     return HttpResponse(json_data, content_type='application/json')
    # json_data = JSONRenderer().render(serializer.errors)
    # return HttpResponse(json_data, content_type='application/json')


    # if request.method == 'PUT':
    #     # pdb.set_trace()
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     id = pythondata.get('id')
    #     pre = Person.objects.get(id=id)
    #     serializer = PersonSerializer(pre, data=pythondata,
    #     partial=True)
    #     if serializer.is_valid():
    #     # pdb.set_trace()
    #      serializer.save()
    #      res = {'msg': 'Data Updated'}
    #      json_data = JSONRenderer().render(res)
    #      return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')




    if request.method == 'DELETE':
        # pdb.set_trace()
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        pre = Person.objects.get(id=id)
        pre.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
       


