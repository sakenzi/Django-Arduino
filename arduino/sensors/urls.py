from django.urls import path
from .views import test_view

urlpatterns = [
    path('api/sensor_data/test/', test_view, name='test_view'),
]