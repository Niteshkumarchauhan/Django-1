# GenericAPIviews and Model Mixin
from .models import Person
from .serializers import PersonSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# List and Create - Pk not required
class LCPersonAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
  # Retrieve ,Update and Delete-pk is required
  
class RUDPersonAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)