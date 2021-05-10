from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View


class Research(TemplateView):
    template_name = 'research_platform.html'

    def get_context_data(self, **kwargs):
        context = super(Research, self).get_context_data(**kwargs)
        return context


class ResearchIntelligense(TemplateView):
    template_name = 'research_intelligense.html'

    def get_context_data(self, **kwargs):
        context = super(ResearchIntelligense, self).get_context_data(**kwargs)
        return context


class Scientific(TemplateView):
    template_name = 'scientific_papers.html'

    def get_context_data(self, **kwargs):
        context = super(Scientific, self).get_context_data(**kwargs)
        return context


class TopResearches(TemplateView):
    template_name = 'top_researches.html'

    def get_context_data(self, **kwargs):
        context = super(TopResearches, self).get_context_data(**kwargs)
        return context


class WebinarsView(TemplateView):
    template_name = 'webinars.html'

    def get_context_data(self, **kwargs):
        context = super(WebinarsView, self).get_context_data(**kwargs)
        return context
