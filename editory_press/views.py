from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, DetailView



class HomeView(TemplateView):
    template_name = 'editoryPress/index.html'

    # def get_context_data(self, **kwargs):
        # context = super(HomeView, self).get_context_data(**kwargs)
        # context['form'] = ConsultationForm()
        # return context

