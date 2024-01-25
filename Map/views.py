from django.shortcuts import render, redirect
import folium
from folium.plugins import FastMarkerCluster
from Map.models import EVChargingLocation

# Create your views here.
def index(request):
    stations = EVChargingLocation.objects.all()

    m = folium.Map(location=[41.5025, -72.699997], zoom_start=9)

    latitudes = [station.latitude for station in stations]
    longitudes = [station.longitude for station in stations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    context = {'map': m._repr_html_()}

    return render(request, 'template/base.html', context)