# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SensorSerializer, MeasurementSerializer, SensorListSerializer
from .models import Sensor, Measurement

class SensorsView(ListAPIView):
    '''
    получение всех датчиков и запись нового
    '''
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def post(self, request):
        ser = SensorListSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorInfo(RetrieveAPIView):
    '''
    изменение полей датчика по номеру первичного ключа
    '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = self.get_object()
        ser = SensorSerializer(sensor, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementView(ListAPIView):
    '''
    получение всех измерений и запись нового измерения
    '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        ser = MeasurementSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementInfo(RetrieveAPIView):
    '''
    получение измерения по номеру первичного ключа
    '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer