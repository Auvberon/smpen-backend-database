from django.contrib import admin
from .models import user, logging, inventory

# Register your models here.

admin.site.register(user)
admin.site.register(inventory)
admin.site.register(logging)

