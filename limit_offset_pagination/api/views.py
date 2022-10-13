from django.shortcuts import render
from .serializers import PersonSerializer
from .models import Person
from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
from .mypagination import MyLimitOffstPaginatin

# Create your views here.
class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # pagination_class = PageNumberPagination
    pagination_class = MyLimitOffstPaginatin