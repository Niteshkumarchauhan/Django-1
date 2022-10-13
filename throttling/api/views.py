from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import JackRateThrottle

class PersonModelViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAuthenticatedOrReadOnly]
  # throttle_classes =[AnonRateThrottle, UserRateThrottle]
  throttle_classes =[AnonRateThrottle, JackRateThrottle]
 
