from django.urls import path, include
from .views import login_api, login_validate_api, join_api

urlpatterns = [
    path('login/', login_api),
    path('login/validate/', login_validate_api),
    path('join/', join_api),
]