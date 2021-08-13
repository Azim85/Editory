from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.shortcuts import reverse
from pages.models import Topic

class StaticViewSitemap(Sitemap):
    i18n = True

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='editory.org', name='editory.org')
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)

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

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='editory.org', name='editory.org')
        return super(ArticleSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Topic.objects.all()

    
    