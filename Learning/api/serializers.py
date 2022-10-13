from rest_framework import serializers
class PersonSerializer(serializers.Serializer):
      id = serializers.IntegerField()
      name = serializers.CharField(max_length=30)
      roll = serializers.IntegerField()
