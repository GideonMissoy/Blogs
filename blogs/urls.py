from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('detail/', blogDetail, name='detail'),
    path('category/', blogCategory, name='category'),
]