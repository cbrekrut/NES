from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'hourly'

    def items(self):
        return ['index','contact']
    def priority(self, item):
        priorities = {
            'index': 1.0,
            'contact': 0.6,
            
        }
        return priorities.get(item, 0.5)
    def location(self, item):
        return reverse(item)