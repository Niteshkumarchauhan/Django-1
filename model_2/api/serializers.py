from dataclasses import field
from rest_framework import serializers
from .models import Person


# Validators

def  start_with_r(value):
    if value[0].lower != 'r':
        raise serializers.ValidationError('name should be start with R')
class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model= Person
    fields=['name', 'roll']
   

# Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value    
   
# object level validation
    def validate(self, data):
        nm= data.get('name')
        rl= data.get(150)
        if nm.lower()=='rahul' and rl.lower!='rahul':
         raise serializers.ValidationError('must be rahul')
        return data
