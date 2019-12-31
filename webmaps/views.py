from django.shortcuts import render

from .models import (WebMaps, WebMapsRecord)
from .forms import WebMapsModelForms
# Create your views here.
def home(request):
    template_name = "webmaps/home.html"
    context = {}
    form = WebMapsModelForms(request.POST or None)

    if form.is_valid():
        obj = form.save()
        latitude = form.cleaned_data.get("latitude")
        longtitude = form.cleaned_data.get("longtitude")
        zoom = form.cleaned_data.get("zoom")
        webmaps_obj = WebMaps.objects.filter(**form.cleaned_data)
        user = None
        if request.user.is_authenticated:
            user = request.user
        WebMapsRecord.objects.create(user=user, map=webmaps_obj)
        #create_webmaps(latitude,longtitude,zoom,webmaps_obj)
        form = WebMapsModelForms()
    context["form"] = form

    return render(request, template_name, context)

def create_webmaps(latitude,longtitude,zoom,webmaps_obj):
    import os
    import folium

    lat = set(latitude).replace(".","_")
    long = set(longtitude).replace(".","_")
    zo = set(zoom)
    maps = "{}-{}-{}.html".format(lat,long,zo)

    map_path = os.path.join(settings.BASE_DIR,'webmaps','generated_maps',maps)
    map = folium.Map(width=750, height=500,location=[latitude, longtitude],zoom_start=zoom)

    fg = folium.FeatureGroup(name="My Map")

    fg.add_child(folium.Marker(location=[28.7041, 77.1025],icon=folium.Icon(color='green')))
    map.add_child(fg)

    map.save(map_path)
