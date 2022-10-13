from rest_framework import serializers
from .models import Person
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get ('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get ('roll',instance.roll)
        instance.save()
        return instance

   
