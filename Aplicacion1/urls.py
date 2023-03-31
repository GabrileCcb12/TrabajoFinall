from django.urls import path
from .views import home, mensaje

urlpatterns = [
    path('', home, name="index"),
    path('confirmar', mensaje, name = 'confirmado')

]