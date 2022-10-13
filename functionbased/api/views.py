from urllib import response
from django import views
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view()
# def hello_word(request):
#     return Response({'msg': 'hello word'})

@api_view(['GET','POST'])
def hello_word(request):
    if request.method == 'GET':
        return Response({'msg': 'This is GET request'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is POST request','data': request.data})

