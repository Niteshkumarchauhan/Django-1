from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# model object single data
def person_detail(requests, pk):
    pre = Person.objects.get(id = pk)
    serializer = PersonSerializer(pre)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)
#quary set =all person data

def person_list(requests):
    pre = Person.objects.all()
    serializer = PersonSerializer(pre, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)

