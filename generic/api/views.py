# GenericAPIviews and Model Mixin
from .models import Person
from .serializers import PersonSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin



class PersonList(GenericAPIView, ListModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
class PersonCreate(GenericAPIView, CreateModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class PersonRetrieve(GenericAPIView, RetrieveModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  
class PersonUpdate(GenericAPIView, UpdateModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)


class PersonDestroy(GenericAPIView, DestroyModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)