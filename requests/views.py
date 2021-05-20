from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

    def post(self, request):
        print(request.POST)



class ConsultationView(View):
    def post(self, request):
        form = ConsultationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                done = form.save()
                if done:
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('pages:home')
            else:    
                return render(request,'home.html', {'validated':'validated', 'form':form})
        else:
            return redirect('users:login')

class FreeConsultationView(View):
   def post(self, request):
        form = FreeConsultationForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                done = form.save()
                if done:
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('requests:conferences')
            else:    
                return render(request,'conferences.html', {'validated':'validated', 'form':form})
        else:
            return redirect('users:login')
