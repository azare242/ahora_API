from django.urls import path
from .views import submit_request, get_status

urlpatterns = [
    path("submit/", submit_request, name='submit_request'),
    path("status/", get_status, name="status")
]
