from django.urls import path
from .views import *

app_name = 'store'
urlpatterns = [
    path('',About,name='about'),
]
