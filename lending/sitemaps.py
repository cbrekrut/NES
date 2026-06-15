from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        # Публичные индексируемые страницы. thanks исключён (noindex).
        return ['index', 'prices', 'portfolio', 'contact']

    def priority(self, item):
        priorities = {
            'index': 1.0,
            'prices': 0.9,
            'portfolio': 0.8,
            'contact': 0.6,
        }
        return priorities.get(item, 0.5)

    def location(self, item):
        return reverse(item)
