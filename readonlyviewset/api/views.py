from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets

class PersonReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
 