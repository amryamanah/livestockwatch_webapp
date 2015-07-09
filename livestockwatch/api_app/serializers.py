# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from device_app.models import DeviceCondition, DeviceError, Device


class DeviceConditionSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source="device.name", max_length=20)
    time_taken = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = DeviceCondition
        fields = ('device_name','cpu_usage', 'disk_usage', 'memory_usage', 'time_taken')

    def create(self, validated_data):
        device = get_object_or_404(Device, name=validated_data.get("device").get("name"))

        return DeviceCondition.objects.create(
            device=device,
            cpu_usage=validated_data.get("cpu_usage"),
            disk_usage=validated_data.get("disk_usage"),
            memory_usage=validated_data.get("memory_usage"),
            time_taken=validated_data.get("time_taken")
        )

class DeviceErrorSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source="device.name", max_length=20)
    time_taken = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = DeviceError
        fields = ('device_name', 'severity', 'component', 'status', 'message', 'time_taken')

    def create(self, validated_data):
        device = get_object_or_404(Device, name=validated_data.get("device").get("name"))

        return DeviceError.objects.create(
            device=device,
            severity=validated_data.get("severity"),
            component=validated_data.get("component"),
            status=validated_data.get("status"),
            message=validated_data.get("message"),
            time_taken=validated_data.get("time_taken")
        )
