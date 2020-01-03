# this is for testing only
from django.contrib import admin
from django.urls import path

from .views import (
    home,
    display_map
)

urlpatterns = [
    path('', home),
    path('generated_maps/<str:map_name>', display_map),
]
