# GenericAPIviews and Model Mixin
from .models import Person
from .serializers import PersonSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle




class PersonList(ListAPIView):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'lv'
  
  
  
class PersonCreate(CreateAPIView):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'cp'
  
 
  
class PersonRetrieve(RetrieveAPIView):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'pr'
  

  
  
class PersonUpdate(UpdateAPIView):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'up'
  
 

class PersonDestroy(DestroyAPIView):
  queryset = Person.objects.all()
  serializer_class= PersonSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'dp'
  
  