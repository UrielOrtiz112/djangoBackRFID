from django.urls import include, path, re_path
from rest_framework import routers
from rfid import views
from rfid import serializers
urlpatterns = [
    re_path(r'^rfid/$', views.RfidList.as_view()),
    re_path(r'^rfid/(?P<pk>\d+)$', views.RfidDetail.as_view()),
]
