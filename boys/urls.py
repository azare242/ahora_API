from django.urls import path
from .views import Ping, echo, get_all_staff
urlpatterns = [
    path('ping/', Ping.as_view(), name='ping'),
    path('echo/<msg>/', echo, name='echo'),
    path('allstaff/', get_all_staff, name='staff')
    
]
