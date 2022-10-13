from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework.generics import ListAPIView
from .models import Person
# Create your views here.

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    def get_queryset(self):
        user =self.request.user
        return Person.objects.filter(passby=user)