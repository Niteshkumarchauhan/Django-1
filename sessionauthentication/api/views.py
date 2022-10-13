from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions

class PersonModelViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  authentication_classes = [SessionAuthentication]
  # permission_classes = [IsAuthenticated]
  # permission_classes = [AllowAny]
  # permission_classes = [IsAdminUser]
  # permission_classes = [IsAuthenticatedOrReadOnly]
  # permission_classes = [DjangoModelPermissions]
  # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  permission_classes = [DjangoObjectPermissions]

