from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from device_app.models import Device, DeviceCondition, DeviceLog, DeviceError

from .serializers import DeviceConditionSerializer, DeviceErrorSerializer

@api_view(["GET", "POST"])
def device_condition_list(request, format=None):

    if request.method == "GET":
        lst_device_condition = DeviceCondition.objects.all()
        serializer = DeviceConditionSerializer(lst_device_condition, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DeviceConditionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def device_error_list(request, format=None):

    if request.method == "GET":
        lst_device_condition = DeviceError.objects.all()
        serializer = DeviceErrorSerializer(lst_device_condition, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DeviceErrorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


