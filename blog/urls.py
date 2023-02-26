from django.urls import path
from .views import *


urlpatterns = [
    path('', StartPage.as_view(), name='home')
]
