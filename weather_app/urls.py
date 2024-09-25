from django.urls import path
from .views import weather_function

urlpatterns = [
    path('city/<str:city>/', weather_function, name='city')
]