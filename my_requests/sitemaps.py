from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class RequestSitemap(Sitemap):
    i18n = True

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