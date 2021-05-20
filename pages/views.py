from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
from django.views.generic import TemplateView, View, DetailView
from .models import Topic, TopResearches
from requests.forms import ConsultationForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = ConsultationForm()
        return context


class Article(DetailView):
    template_name = 'article.html'
    model = Topic
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        context['get_by_theme'] = Topic.objects.filter(
            material_name=self.object.material_name).exclude(pk=self.object.pk)[:3]
        return context


class Articles(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        random_topic = []
        last_week = []
        k = datetime.datetime.today() - datetime.timedelta(days=7)
        for i in Topic.objects.all():
            random_topic.append(i)
            if (k.month == i.created_at.month and k.year == i.created_at.year) and k.day < i.created_at.day:
                last_week.append(i)
        try:
            top_8 = Topic.objects.order_by('-created_at')[:9]

            context = super(Articles, self).get_context_data(**kwargs)
            context['top_4'] = Topic.objects.order_by('-created_at')[:4]
            context['random_topic'] = random.choice(random_topic)
            context['last_week'] = last_week[:6]
            context['top_8'] = top_8
        except:
            pass
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['form'] = ConsultationForm()
        return context


class Paper(DetailView):
    template_name = 'paper.html'
    model = TopResearches
    context_object_name = 'single_research'

    def get_context_data(self, **kwargs):
        context = super(Paper, self).get_context_data(**kwargs)
        return context


class Services(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super(Services, self).get_context_data(**kwargs)
        return context


class Dissertation(TemplateView):
    template_name = 'dissertation.html'

    def get_context_data(self, **kwargs):
        context = super(Dissertation, self).get_context_data(**kwargs)
        return context


class Research_strategy(TemplateView):
    template_name = 'research_strategy.html'

    def get_context_data(self, **kwargs):
        context = super(Research_strategy, self).get_context_data(**kwargs)
        context['form'] = ConsultationForm()
        return context


class Language_editing(TemplateView):
    template_name = 'language_editing.html'

    def get_context_data(self, **kwargs):
        context = super(Language_editing, self).get_context_data(**kwargs)
        return context
