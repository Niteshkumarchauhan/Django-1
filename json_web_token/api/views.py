from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class PersonModelViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
 
