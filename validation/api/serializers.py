from rest_framework import serializers
from .models import Person


# Validators

def  start_with_r(value):
    if value[0].lower != 'r':
        raise serializers.ValidationError('name should be start with R')
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, validators=[start_with_r])
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

# Validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value    
   
# object level validation
    def validate(self, data):
        nm= data.get('name')
        rl= data.get(150)
        if nm.lower()=='rahul' and rl.lower!='rahul':
         raise serislizers.ValidationError('must be rahul')
        return data
