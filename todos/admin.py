""" Todo Admin Definition"""
from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    """ Todo Admin Definition """
    list_display = (
        'title',
        'body',
    )

admin.site.register(Todo, TodoAdmin)
# Register your models here.
