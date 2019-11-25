from rest_framework import serializers
from asistencia.models import asistencia 

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = asistencia
        fields = ('__all__')
