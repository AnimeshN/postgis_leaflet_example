from django.shortcuts import render
from django.core.serializers import serialize
from .models import Ward61OsmBuildings

def home(req):
    obj = Ward61OsmBuildings.objects.all()
    geojson = serialize('geojson',obj)
    context = {'geojson':geojson}
    return render(req,"home/index.html",context)
