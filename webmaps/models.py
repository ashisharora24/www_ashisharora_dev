from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class WebMaps(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    zoom = models.IntegerField()

    def __str__(self):
        lat = set(self.latitude).replace(".","_")
        long = set(self.longtitude).replace(".","_")
        zo = set(self.zoom)
        return "{}-{}-{}.html".format(lat,long,zo)

    def get_absolut_map_url(self):
        lat = set(self.latitude).replace(".","_")
        long = set(self.longtitude).replace(".","_")
        zo = set(self.zoom)
        maps = "{}-{}-{}.html".format(lat,long,zo)

        return f"/webmaps/generated_maps/{maps}.html"

class WebMapsRecord(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    map = models.ForeignKey(WebMaps, on_delete=models.CASCADE)
