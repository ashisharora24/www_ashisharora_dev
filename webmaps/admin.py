from django.contrib import admin

# Register your models here.
from .models import (WebMaps, WebMapsRecord)

admin.site.register(WebMaps)
admin.site.register(WebMapsRecord)
