from django.shortcuts import render, redirect
import folium
from folium.plugins import FastMarkerCluster, LocateControl, Geocoder, MarkerCluster
from Map.models import EVChargingLocation
from folium import Marker

# Create your views here.
def index(request):
    stations = EVChargingLocation.objects.all()

    m = folium.Map(location=[41.5025, -72.699997], zoom_start=9, tiles="cartodbpositron", attr="Electric Charging Stations")

    latitudes = [station.latitude for station in stations]
    longitudes = [station.longitude for station in stations]
    stationNames = [station.station_name for station in stations]

    evcSimpleMarkers = folium.FeatureGroup(name="EVC Stations", show=True).add_to(m)

    # FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(evcSimpleMarkers)

    for station in stations:
        coordinates = (station.latitude, station.longitude)
        MarkerCluster().add_child(
            folium.Marker(
                coordinates,
                popup="Station: " + station.station_name,
                icon=folium.Icon(icon='car', prefix='fa'),
                tooltip="Station: " + str(station.station_name)
                )
        ).add_to(evcSimpleMarkers)
        
    folium.LayerControl(position='bottomright').add_to(m)
    LocateControl().add_to(m)
    Geocoder().add_to(m)
    folium.LatLngPopup().add_to(m)

    context = {'map': m._repr_html_()}

    return render(request, 'template/base.html', context)