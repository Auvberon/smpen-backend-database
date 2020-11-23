from django.contrib import admin
from .models import logging, inventory

# Register your models here.

admin.site.register(inventory)
admin.site.register(logging)

