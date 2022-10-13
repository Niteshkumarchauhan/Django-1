# from ast import Return
# from distutils.log import error
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse       
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.response import Response
# JsonResponse
# import pdb
@csrf_exempt
def person_create(request):
    if request.method == 'POST':
        # pdb.set_trace()
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
        # return Response("ok")
        # return JsonResponse(serializer.data)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')