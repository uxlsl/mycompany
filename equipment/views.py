from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Driver
from .serializers import CarSerializer, DriverSerializer



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer



def car_dirvers(request, pk, dirver_pk=None):
    car = Car.objects.get(pk=pk)
    if dirver_pk is None:
        serializer = DriverSerializer(car.drivers.all(), many=True)
    else:
        serializer = DriverSerializer(car.drivers.get(pk=dirver_pk), many=False)
    return JsonResponse(serializer.data, safe=False)
