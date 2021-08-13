from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.shortcuts import reverse

class RequestSitemap(Sitemap):
    i18n = True

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='editory.org', name='editory.org')
        return super(RequestSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return [
            'requests:research',
            'requests:research_intelligense',
            'requests:scientific-papers',
            'requests:conferences',
            'requests:creat-conferences',
            'requests:grants',
            'requests:patents',
            'requests:bak',
            'requests:scopus',
            'requests:proofreading',
            'requests:design',
            'requests:translation'   
        ]

    def location(self, item):
        return reverse(item)    