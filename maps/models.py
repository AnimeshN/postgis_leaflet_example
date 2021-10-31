from django.contrib.gis.db import models

class Ward61OsmBuildings(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    fid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    osm_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    building_t = models.CharField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    num_flats = models.BigIntegerField(blank=True, null=True)
    wing = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ward61_osm_buildings'