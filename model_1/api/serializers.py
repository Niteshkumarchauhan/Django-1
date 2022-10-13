from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
  # name=serializers.CharField(read_only=True)
  class Meta:
    model= Person
    fields=['name', 'roll']
    # read_only_fields =['name', 'roll']
    extra_kwargs ={'name':{'read_only':True}}