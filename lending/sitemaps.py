from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'hourly'

    def items(self):
        # Перечислите здесь все статические URL, которые вы хотите включить
        return ['home','about','contact']
    def priority(self, item):
        # Устанавливаем разный приоритет для разных страниц
        priorities = {
            'home': 1.0,
            'about': 0.8,
            'contact': 0.6,
        }
        return priorities.get(item, 0.5)
    def location(self, item):
        return reverse(item)