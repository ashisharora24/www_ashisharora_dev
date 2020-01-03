from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class WebMaps(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    zoom = models.IntegerField()

    def __str__(self):
        lat = str(self.latitude).replace(".","_")
        long = str(self.longtitude).replace(".","_")
        zo = str(self.zoom)
        return "{}-{}-{}.html".format(lat,long,zo)

    # get absolute url
    def get_absolut_map_url(self):
        lat = str(self.latitude).replace(".","_")
        long = str(self.longtitude).replace(".","_")
        zo = str(self.zoom)
        maps = "{}-{}-{}.html".format(lat,long,zo)

        return f"/webmaps/generated_maps/{maps}.html"

# webMapsRecords

class WebMapsRecord(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    map = models.ForeignKey(WebMaps, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.user,self.map)
