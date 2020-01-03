from django.shortcuts import render

from .models import (WebMaps, WebMapsRecord)
from .forms import WebMapsModelForms
from django.conf import settings


# Create your views here.

def home(request):

    map_name = ""
    create_map = False
    template_name = "webmaps/home.html"
    context = {}
    form = WebMapsModelForms(request.POST or None)


    if form.is_valid():
        # we will update the record later
        obj = form.save(commit=False)

        #print(**form.cleaned_data)
        webmaps_obj = WebMaps.objects.filter(**form.cleaned_data)

        if webmaps_obj.count()==1:
            # means that the map for these values already exist
            map_name = get_file_name(str(webmaps_obj))
            # check if the file exist
            if check_if_file_exist(map_name)==False:
                create_map = True
        else:
            create_map = True

        latitude = form.cleaned_data.get("latitude")
        longtitude = form.cleaned_data.get("longtitude")
        zoom = form.cleaned_data.get("zoom")
        if create_map == True:

            if map_name=="":
                map_name = get_map_name(latitude,longtitude,zoom)
                obj = form.save()
            create_webmaps(latitude,longtitude,zoom,map_name)

        # updating the records of the search
        user = None
        if request.user.is_authenticated:
            user = request.user

        WebMapsRecord.objects.create(user=user, map=WebMaps.objects.get(latitude=float(latitude), longtitude=float(longtitude),zoom=zoom))

        form = WebMapsModelForms()

    context["form"] = form

    # sending the map_name to the html page
    context['map_name']=map_name

    return render(request, template_name, context)


def get_map_name(latitude,longtitude,zoom):
    '''
        generate the map file name .
    '''
    lat = str(float(latitude)).replace(".","_")
    long = str(float(longtitude)).replace(".","_")
    zo = str(zoom)
    return "{}-{}-{}.html".format(lat,long,zo)


def create_webmaps(latitude,longtitude,zoom,map_name):
    '''
        generate the map files
    '''
    import os
    import folium

    map_path = os.path.join(settings.BASE_DIR,'webmaps','templates','webmaps','generated_maps',map_name)
    # map = folium.Map(width=100%, height=100%,location=[latitude, longtitude],zoom_start=zoom)
    map = folium.Map(location=[latitude, longtitude],zoom_start=zoom)

    fg = folium.FeatureGroup(name="My Map")

    #fg.add_child(folium.Marker(location=[28.7041, 77.1025],icon=folium.Icon(color='green')))
    map.add_child(fg)

    # path = 'C:\\workstation\\ashish_arora_workstation\\www_ashisharora_dev\\webmaps\\templates\\webmaps\\created_webmaps'+map_name
    map.save(map_path)



def get_file_name(str):
    '''
        get file name from the object query
    '''
    print("str : ",str)
    import re
    x = re.search(r'\<QuerySet \[<WebMaps: (.*)\>\]\>', str)
    return x.group(1)


def check_if_file_exist(map_name):
    '''
        check if the file name exist or not
    '''

    import os.path
    from os import path
    # print(map_name)

    map_path = os.path.join(settings.BASE_DIR,'webmaps','generated_maps',map_name)

    return path.exists(map_path)


def display_map(request, map_name):
    '''
        display map on the next blank tab
    '''
    template_name = 'webmaps/generated_maps/'+map_name
    context = {}
    return render(request, template_name, context)
