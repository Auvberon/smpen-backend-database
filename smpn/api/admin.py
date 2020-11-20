from django.contrib import admin
from .models import user, inventory, logging

# Register your models here.

admin.site.register(user)
admin.site.register(inventory)
admin.site.register(logging)

