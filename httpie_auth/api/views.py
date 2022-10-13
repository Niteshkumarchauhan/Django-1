from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class PersonModelViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  authentication_classes = [TokenAuthentication]
  # permission_classes = [IsAuthenticated]
  permission_classes = [IsAuthenticatedOrReadOnly]
 
