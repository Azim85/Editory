from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
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
        last_week = []
        k = datetime.datetime.today() - datetime.timedelta(days=7)
        for i in Topic.objects.all():
            random_topic.append(i)
            if (k.month == i.created_at.month and k.year == i.created_at.year) and k.day < i.created_at.day:
                last_week.append(i)
            print(k.day)
            print(i.created_at.day)
        
        top_8 = Topic.objects.order_by('-created_at')[:9]

        context = super(News, self).get_context_data(**kwargs)
        context['top_4'] = Topic.objects.order_by('-created_at')[:4]
        context['random_topic'] = random.choice(random_topic)
        context['last_week'] = last_week[:6]
        context['top_8'] = top_8
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        return context
