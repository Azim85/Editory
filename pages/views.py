import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
import random
import datetime
from django.contrib import messages
from django.views.generic import TemplateView, View, DetailView, ListView
from .models import Topic, TopResearches, About_us_news, Tariffs
from my_requests.forms import ConsultationForm, OrganizeResearchForm, LanguageForm
from .forms import ResumeForm, TopicForm
from orders.forms import OrderForm
from users.models import Colleague, CustomUser
from django.http import JsonResponse
import sys, glob, os
from django.core.files import File
from django.conf import settings
from setpage.models import AboutUsModel, ContactModel, LangEditModel, ResearchStrategyModel
from setpage.forms import AboutUSForm, ContactForm, LangForm

from dateutil.rrule import rrule, MONTHLY

import logging

logger = logging.getLogger(__name__)


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
        topic = Topic.objects.get(pk=self.kwargs['pk'])
        context = super(Article, self).get_context_data(**kwargs)
        self.request.breadcrumb = topic.title
        context['get_by_theme'] = Topic.objects.filter(
            material_name=self.object.material_name).exclude(pk=self.object.id)[:3]
        context['form'] = TopicForm(instance=topic)
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


class AboutUs(View):
    def get(self, request):
        text = AboutUsModel.objects.first()
        about = AboutUSForm(instance=text)
        staffs = Colleague.objects.all()
        form = ResumeForm()
        slick = About_us_news.objects.all()

        context = {'form': form, 'staffs': staffs, 'text': text, 'about': about, "slick": slick}
        return render(request, 'about_us.html', context)

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('pages:webinars')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request, 'about_us.html', {'form': form, "ss": "ss"})
            else:
                return render(request, 'about_us.html', {'form': form, "ss": "ss"})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        return context


class Contact(View):
    def get(self, request):
        text = ContactModel.objects.first()
        form = ContactForm(instance=text)
        return render(request, 'contact.html', {'text': text, 'form': form})


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


class Dissertation(View):

    def get(self, request):
        return render(request, 'dissertation.html')


class Research_strategy(View):

    def get(self, request):
        data = request.GET.get('data')
        # print(pk)
        # message = request.GET.get('pk')
        # kwargs = pk
        text = ResearchStrategyModel.objects.first()
        context = {'forms': OrganizeResearchForm(), 'form': ConsultationForm(), 'raqam': data, 'text': text}
        return render(request, 'research_strategy.html', context)

    def post(self, request):
        forms = OrganizeResearchForm(request.POST)
        if request.user.is_authenticated:
            if forms.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = forms.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('pages:research_strategy')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму')
                    return render(request, 'research_strategy.html', {'forms': forms, 'validated': 'validated'})
            else:
                return render(request, 'research_strategy.html', {'forms': forms})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class Language_editing(View):
    def get(self, request):
        tariffs = Tariffs.objects.all()
        form = OrderForm()
        forms = LanguageForm()
        obj = LangEditModel.objects.first()
        lang = LangForm(instance=obj)
        return render(request, 'language_editing.html', {'form': form, 'forms': forms, 'text': obj,
                                                         'lang': lang, 'tariffs': tariffs})

    def post(self, request):
        forms = LanguageForm(request.POST, request.FILES)

        if forms.is_valid():

            done = forms.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('pages:language_editing')


        return render(request, 'language_editing.html', {'forms': forms})


def get_context_data(self, **kwargs):
    context = super(Language_editing, self).get_context_data(**kwargs)
    return context


class top25(TemplateView):
    template_name = 'scientific_paper/top25.html'


class top2uzb(TemplateView):
    template_name = 'scientific_paper/top2uzb.html'


class top10(TemplateView):
    template_name = 'scientific_paper/top10.html'


class top10uz(TemplateView):
    template_name = 'scientific_paper/top10uz.html'


def change_image(request):
    topic_id = request.POST.get('topic_id')
    image = request.FILES.get('main_image')

    if not image:
        return redirect('pages:article', pk=topic_id)

    topic = Topic.objects.get(pk=topic_id)
    topic.main_image = image
    topic.save()
    return redirect('pages:article', pk=topic_id)


def change_material(request):
    topic_id = request.POST.get('topic_id')
    material = request.POST.get('material_name')

    if not material:
        return redirect('pages:article', pk=topic_id)

    topic = Topic.objects.get(pk=topic_id)
    topic.material_name = material
    topic.save()
    return redirect('pages:article', pk=topic_id)


def change_title(request):
    topic_id = request.POST.get('topic_id')
    title = request.POST.get('title')

    if not title:
        return redirect('pages:article', pk=topic_id)

    topic = Topic.objects.get(pk=topic_id)
    topic.title = title
    topic.save()
    return redirect('pages:article', pk=topic_id)


def change_description(request):
    topic_id = request.POST.get('topic_id')
    description = request.POST.get('description')

    if not description:
        return redirect('pages:article', pk=topic_id)

    topic = Topic.objects.get(pk=topic_id)
    topic.description = description
    topic.save()
    return redirect('pages:article', pk=topic_id)


def change_others(request):
    topic_id = request.POST.get('topic_id')
    others = request.POST.get('others')

    if not others:
        return redirect('pages:article', pk=topic_id)

    topic = Topic.objects.get(pk=topic_id)
    topic.others = others
    topic.save()
    return redirect('pages:article', pk=topic_id)


class allNews(ListView):
    template_name = 'all_news_page.html'
    # model = Topic
    paginate_by = 6
    context_object_name = 'topics'


    def get_queryset(self):
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')

        qs = Topic.objects.all()

        if year and month:
            qs = qs.filter(created_at__year=year, created_at__month=month)

        return qs
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        now = datetime.datetime.now()
        
        end_date, start_date = datetime.datetime(now.year, 12, 1), datetime.date(now.year - 1, 1, 1)

        years = {
            end_date.year: [],
            start_date.year: [],
        }
        for d in rrule(MONTHLY, dtstart=start_date, until=end_date):
            years[d.year].append([d.month, d.strftime('%B')])
            
        context['years'] = years

        return context

        # nows = datetime.datetime.now()
        # old = datetime.datetime(2020, 12, 31 )
        # monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # lst = [ [] for i in monthes ]

        # lst_years = []
        

        # for i in range(old.year, nows.year+1):
        #     lst_years.append(i)
        # k = reversed(lst_years)

        # years = {}

        # for i in range(1, 365):
        #     d = old + datetime.timedelta(days=i)
        #     if d.day == nows.day+1 and d.month == nows.month and d.year == nows.year:
        #         break

        #     for j in monthes:
        #         if monthes.index(j)+1 == d.month: 
        #             lst[monthes.index(j)].append(d)
        #             years[j] = lst[monthes.index(j)]

        # context['years'] = k
        # context['monthes'] = monthes
        # return context

        

    




class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        news = Topic.objects.filter(
            Q(material_name__icontains=q) | Q(title__icontains=q) | Q(description__icontains=q)).distinct()
        return render(request, 'search.html', {'news': news, 'query': q})
