from django.urls import path

from measurement.views import SensorsView, SensorInfo, MeasurementView, MeasurementInfo


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorInfo.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<pk>/', MeasurementInfo.as_view()),

]
