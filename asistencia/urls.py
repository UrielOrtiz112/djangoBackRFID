from django.urls import include, path, re_path
from rest_framework import routers
from asistencia import views
from asistencia import serializers

urlpatterns = [
    re_path(r'^asistencia/$', views.AsistenciaList.as_view()),
    re_path(r'^asistencia/(?P<pk>\d+)$', views.AsistenciaDetail.as_view()),
]
