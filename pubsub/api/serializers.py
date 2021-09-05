from django.contrib.auth.models import User, Group
from rest_framework import serializers
from subpub_emulator import models as subpub


class SerializerDevice(serializers.ModelSerializer):
    class Meta:
        model = subpub.Device
        fields = ['id', 'name', 'device_id', 'latitude', 'longitude', 'status', ]


class SerializerTemperature(serializers.ModelSerializer):
    device = SerializerDevice(read_only=True)

    class Meta:
        model = subpub.Temperature
        fields = ['device', 'time', 'temperature', ]