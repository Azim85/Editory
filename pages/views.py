from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime, timedelta
from django.views.generic import TemplateView, View
from .models import Topic


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class Articles(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(Articles, self).get_context_data(**kwargs)
        return context


class News(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        random_topic = []
        k = []
        for i in Topic.objects.all():
            random_topic.append(i)
            if timedelta(hours=i.created_at) > timedelta(hours=-168):
                k.append(i)

        context = super(News, self).get_context_data(**kwargs)
        context['top_4'] = Topic.objects.order_by('-created_at')[:4]
        context['random_topic'] = random.choice(random_topic)
        print(k)
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        return context
