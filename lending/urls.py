from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/metall-design/',views.md,name='md'),
    path('portfolio/nanopi/',views.nanopi,name='nanopi'),
    path('portfolio/tsg/', views.tsg, name='tsg'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]