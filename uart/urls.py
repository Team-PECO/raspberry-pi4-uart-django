from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manual/', views.manual_control, name='manual'),
    path('automatic/', views.automatic_control, name='automatic'),
    path('send/<str:command>/', views.send_uart_command, name='send_uart_command'),
]
