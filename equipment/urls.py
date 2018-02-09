#!-*- coding:utf-8 -*-

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, car_dirvers


root_router = DefaultRouter()

root_router.register(r'cars', CarViewSet, base_name='cars')

urlpatterns = root_router.urls

urlpatterns.append(
        url(r'cars/(?P<pk>[0-9]+)/dirvers/(?P<dirver_pk>[0-9]+)?',
            car_dirvers))

