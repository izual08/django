from django.urls import path

from . import views

app_name = 'fanwebsite'

urlpatterns = [
    path('', views.index, name='index'),
]
