from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def index(request):
    person1 ={
        'name':'ratul',
        'age':20,
        'is_married':False,
    }
    person1 ={
        'name':'shipon',
        'age':19,
        'is_married':False,
    }
    person_list = [person1,person1]

    return Response(person_list)

@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()

    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request, id):

    todo = get_object_or_404( Todo, id=id)
    serializer = TodoSerializer(todo)


    return Response(serializer.data)


