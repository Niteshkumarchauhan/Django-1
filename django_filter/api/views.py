from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework.generics import ListAPIView
from .models import Person
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    filterset_fields = ['name','roll']
 