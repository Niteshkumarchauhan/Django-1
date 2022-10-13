from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()

    def create(self, validated_data):
      return Person.objects.create(**validated_data)



# def create(self, validate_data):
#  return Person.objects.create(**validate_data)
