from django.urls import path
from .views import (
    submit_request, 
    get_status,
    ping, 
    echo_ip,
    testing,
    )

urlpatterns = [
    path('ping/', ping, name='ping'),
    path("submit/", submit_request, name='submit_request'),
    path("status/", get_status, name="status"),
    path("myip/", echo_ip, name='ip')
    path("test/", testing, name='test')
]
