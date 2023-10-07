from django.urls import path
from .views import submit_request, get_status, ping, test_images

urlpatterns = [
    path('ping/', ping, name='ping'),
    path("submit/", submit_request, name='submit_request'),
    path("status/", get_status, name="status"),
    path("tsimg/", test_images, name='testi')
]
