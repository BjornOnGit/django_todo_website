""" This is the beginning of the serializer module"""

from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """ The Todo serializer class"""
    class Meta:
        """ Defining the serializer fields for the Todo model"""
        model = Todo
        fields = (
            'id',
            'title',
            'body',
        )
