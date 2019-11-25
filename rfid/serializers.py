from rest_framework import serializers
from rfid.models import rfid

class RfidSerializer(serializers.ModelSerializer):
    class Meta:
        model = rfid
        fields = ('__all__')
