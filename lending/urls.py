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
    path('portfolio/metall-design/',views.md,name='md'),
    path('portfolio/nanopi/',views.nanopi,name='nanopi'),
    path('portfolio/tsg/', views.tsg, name='tsg'),
    path('portfolio/priliv/', views.priliv, name='priliv'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]