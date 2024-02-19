from django.contrib import admin
from django.urls import path, include
from Map.views import *

urlpatterns = [
    path("", index, name="index"),
    path('home', products, name='home'),
    path('ev-station/<int:station_id>/', redirect_to_station, name='ev'),
]