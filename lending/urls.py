from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tsg/', views.tsg, name='tsg'),
    path('portfolio/', views.portfolio, name='portfolio'),
]