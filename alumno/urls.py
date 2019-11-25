from django.urls import include, path, re_path
from rest_framework import routers
from alumno import views
from alumno import serializers

urlpatterns = [
    re_path(r'^alumno/$', views.AlumnoList.as_view()),
    re_path(r'^alumno/(?P<pk>\d+)$', views.AlumnoDetail.as_view()),
]
