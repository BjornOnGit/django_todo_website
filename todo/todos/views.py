""" The beginning of the Todo views module """
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    """ This view lists all of the Todo items """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    """ This view gives the Todo items by id. """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
