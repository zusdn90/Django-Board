from django.urls import path
from .views import post_list_api

urlpatterns = [
    path('', post_list_api),
]