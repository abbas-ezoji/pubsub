from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from subpub_emulator import models as subpub
from . import serializers


@permission_classes([AllowAny, ])
class Devices(generics.ListAPIView):
    queryset = subpub.Device.objects.all()
    serializer_class = serializers.SerializerDevice

    def get_queryset(self):
        d_id = int(self.request.GET.get('id', 0))
        if d_id:
            device = subpub.Device.objects.all().filter(pk=d_id)
        else:
            device = subpub.Device.objects.all()

        return device


@permission_classes([AllowAny, ])
class DevicesAgg(generics.ListAPIView):
    queryset = subpub.Temperature.objects.all()
    serializer_class = serializers.SerializerDevice

    def get_queryset(self):
        d_id = int(self.request.GET.get('id', 0))
        if d_id:
            device = subpub.Device.objects.all().filter(pk=d_id)
        else:
            device = subpub.Device.objects.all()

        return device