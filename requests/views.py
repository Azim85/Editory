from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from pages.models import TopResearches
from .forms import ConsultationForm, FreeConsultationForm


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


class TopResearchess(TemplateView):
    template_name = 'top_researches.html'

    def get_context_data(self, **kwargs):
        context = super(TopResearchess, self).get_context_data(**kwargs)
        context['top_researches'] = TopResearches.objects.all()
        return context


class WebinarsView(TemplateView):
    template_name = 'webinars.html'

    def get_context_data(self, **kwargs):
        context = super(WebinarsView, self).get_context_data(**kwargs)
        return context


class Conferences(View):
    def get(self, request):
        context = {'form':FreeConsultationForm()}
        return render(request, 'conferences.html', context)

    def get_context_data(self, **kwargs):
        context = super(Conferences, self).get_context_data(**kwargs)
        return context


class ConsultationView(View):
    def post(self, request):
        validated = False
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            validated = True
        return render(request, 'home.html', {'form':form, 'validated':validated})
