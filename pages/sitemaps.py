from django.conf.urls import i18n
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from pages.models import Topic

class StaticViewSitemap(Sitemap):
    i18n = True

    def items(self):
        return [
            'pages:home', 
            'pages:webinars',
            'pages:news',
            'pages:services',
            'pages:dissertation',
            'pages:research_strategy',
            'pages:language_editing',
            'pages:contact',
            'pages:allnews'
            ]

    def location(self, item):
        return reverse(item)
    

class ArticleSitemap(Sitemap):
    i18n = True

    def items(self):
        return Topic.objects.all()

    
    