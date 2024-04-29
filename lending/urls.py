from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from . import views


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:id>/', views.portfolio_ident, name='portfolio_ident'),
    path('contact/', views.contact, name='contact'),
    path('prices/', views.prices, name='prices'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('thanks/', views.thanks, name='thanks'),
]