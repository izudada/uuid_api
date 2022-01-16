from django.urls import path
from .views import CowrywiseAPI


urlpatterns = [
    path('', CowrywiseAPI.as_view(), name="customers")
]
