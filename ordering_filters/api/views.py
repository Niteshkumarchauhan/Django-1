from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework.generics import ListAPIView
from .models import Person
from rest_framework.filters import OrderingFilter
# Create your views here.

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    filter_backends = [OrderingFilter]
    # ordering_fields =['name']
    ordering_fields =['name','roll']
   
    
   
 