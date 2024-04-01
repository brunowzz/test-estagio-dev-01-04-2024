from django.urls import path
from calculator.views import calcular_economia

urlpatterns = [
    path('', calcular_economia, name='calcular_economia'),
]
