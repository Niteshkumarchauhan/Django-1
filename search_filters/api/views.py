from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework.generics import ListAPIView
from .models import Person
from rest_framework.filters import SearchFilter
# Create your views here.

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    filter_backends = [SearchFilter]
    # search_fields = ['name']
    # search_fields = ['name','roll']
    search_fields = ['^name']
    
   
 