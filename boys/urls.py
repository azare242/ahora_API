from django.urls import path
from .views import Ping, echo, payment, verify_payment
urlpatterns = [
    path('ping/', Ping.as_view(), name='ping'),
    path('echo/<msg>/', echo, name='echo'),
    
]
