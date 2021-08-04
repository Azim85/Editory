from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, View
from pages.models import TopResearches, WebinarsUrl1, WebinarsUrl2
from .forms import (ConsultationForm, FreeConsultationForm, ProofreadingForm,
                    PeerReviewForm, OrganizeConferencesForm, BaksForm, TranslationForm, PatentsForm, GrantsForm,  ScopusesForm)
from .models import Translation
from setpage.forms import WebinarsForm, TranslationsForm
from setpage.models import WebinarsModel, TranslationModel

from setpage.models import (BakModel, ConferencesModel, CreateConferenceModel, DesignModel, GrantsModel,
                            PatentModel, ScopusModel, ProofModel)
from setpage.forms import BakForm, ConferencesForm, CreateConferenceForm, DesignForm, GrantForm, PatentForm, ScopusForm, \
    ProofForm


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
        text = WebinarsModel.objects.first()
        context['webinar'] = WebinarsForm(instance=text)
        context['text'] = text
        context['url1'] = WebinarsUrl1.objects.all()
        context['url2'] = WebinarsUrl2.objects.all()
        return context


# todo yangilash
class Conferences(View):
    def get(self, request):
        text = ConferencesModel.objects.first()
        con = ConferencesForm(instance=text)
        context = {'form': FreeConsultationForm(), 'con': con, 'text': text}
        return render(request, 'conferences.html', context)

    def post(self, request):
        form = FreeConsultationForm(request.POST, request.FILES)

        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('requests:conferences')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request, 'conferences.html', {'validated': 'validated', 'form': form})
            else:
                return render(request, 'conferences.html', {'validated': 'validated', 'form': form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')



class CreateConferences(View):
    def get(self, request):
        text = CreateConferenceModel.objects.first()
        con = CreateConferenceForm(instance=text)
        context = {'form': OrganizeConferencesForm(), 'text': text, 'con': con}
        return render(request, 'creat_conference.html', context)

    def post(self, request):
        form = OrganizeConferencesForm(request.POST)
        if form.is_valid():  
            done = form.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('requests:creat-conferences')
        return render(request, 'creat_conference.html', {'validated': 'validated', 'form': form})
      

class Design(View):
    def get(self, request):
        obj = DesignModel.objects.first()
        design = DesignForm(instance=obj)
        context = {'form': GrantsForm(), 'text': obj, 'design': design}
        return render(request, 'design.html', context)

    def post(self, request):
        form = GrantsForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save(commit=False)
                    done.theme = request.POST.get('theme')
                    done.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('requests:design')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request, 'design.html', {'validated': 'validated', 'form': form})
            else:
                return render(request, 'design.html', {'validated': 'validated', 'form': form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class ConsultationView(View):
    def get(self, request):
        form = FreeConsultationForm()
        return render(request, 'conferences.html', {'form': form})

    def post(self, request):
        form = FreeConsultationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('requests:consultation')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request, 'conferences.html', {'validated': 'validated', 'form': form})
            else:
                return render(request, 'conferences.html', {'validated': 'validated', 'form': form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


# class FreeConsultationView(View):
#    def post(self, request):
#         form = FreeConsultationForm(request.POST, request.FILES)
#         if request.user.is_authenticated:
#             if form.is_valid():
#                 if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
#                     done = form.save()
#                     if done:
#                         messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
#                         return redirect('requests:conferences')
#                 else:
#                     messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
#                     return render(request,'conferences.html', {'validated':'validated', 'form':form})
#             else:
#                 return render(request,'conferences.html', {'validated':'validated', 'form':form})
#         else:
#             messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
#             return redirect('users:login')


class Proofreading(View):
    def get(self, request):
        data = request.GET.get('data')
        obj = ProofModel.objects.first()
        proof = ProofForm(instance=obj)
        context = {'form': ProofreadingForm(), 'raqam': data, 'text': obj, 'proof': proof}
        return render(request, 'proofreading.html', context)

    def post(self, request):

        form = ProofreadingForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                done = form.save()
                if done:
                    print(request.POST)
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('requests:proofreading')
            return render(request, 'proofreading.html', {'form': form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class Peer_review(View):
    def get(self, request):
        context = {'form': PeerReviewForm()}
        return render(request, 'peer_review.html', context)

    def post(self, request):
        form = PeerReviewForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                done = form.save()
                if done:
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('requests:peer_review')
            return render(request, 'peer_review.html', {'form': form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class BAKView(View):
    def get(self, request):
        obj = BakModel.objects.first()
        bak = BakForm(instance=obj)
        form = BaksForm()

        return render(request, 'bak.html', {'form': form, 'bak': bak, 'text': obj})

    def post(self, request):
        form = BaksForm(request.POST)
        
        if form.is_valid():
            done = form.save(commit=False)
            done.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('requests:bak')
        return render(request, 'bak.html', {'validated': 'validated', 'form': form})
       

# updated
class ScopusView(View):
    def get(self, request):
        form = ScopusesForm()

        obj = ScopusModel.objects.first()
        scopus = ScopusForm(instance=obj)
        return render(request, 'scopus.html', {'form': form, 'text': obj, 'scopus': scopus})

    def post(self, request):
        form = ScopusesForm(request.POST)
        if form.is_valid():
            done = form.save(commit=False)
            done.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('requests:scopus')
                
        return render(request, 'scopus.html', {'validated': 'validated', 'form': form})
       

class GrantsView(View):
    def get(self, request):
        obj = GrantsModel.objects.first()
        grant = GrantForm(instance=obj)
        form = GrantsForm()

        return render(request, 'grants.html', {'form': form, 'text': obj, 'grant': grant})

    def post(self, request):
        form = GrantsForm(request.POST, request.FILES)
        
        if form.is_valid():
            done = form.save(commit=False)
            done.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('requests:grants')
            
        return render(request, 'grants.html', {'validated': 'validated', 'form': form})
    

class PatentsView(View):
    def get(self, request):
        form = PatentsForm()

        obj = PatentModel.objects.first()
        patent = PatentForm(instance=obj)
        return render(request, 'patents.html', {'form': form, 'text': obj, 'patent': patent})

    def post(self, request):
        form = PatentsForm(request.POST, request.FILES)
        
        if form.is_valid():
            done = form.save(commit=False)
            done.save()
            if done:
                messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                return redirect('requests:patents')
        return render(request, 'patents.html', {'validated': 'validated', 'form': form})
    


class TranslationView(View):
    def get(self, request):
        text = TranslationModel.objects.first()
        translations = TranslationsForm(instance=text)

        form = TranslationForm()
        return render(request, 'translation.html', {'form': form, 'text': text, 'translations': translations})

    def post(self, request):
        form = TranslationForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            user = request.user
            word_amount = request.POST.get('word_amount')
            language = request.POST.get('language')
            research_area = request.POST.get('research_area')
            extra = request.POST.get('extra')
            comment = request.POST.get('comment')
            file = request.FILES.get('file')

            if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                is_agree = True
                done = Translation.objects.create(user=user, word_amount=word_amount, language=language,
                                                  research_area=research_area, extra=extra, comment=comment, file=file,
                                                  is_agree=is_agree)
                if done:
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('requests:translation')
            else:
                messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                return render(request, 'translation.html', {'validated': 'validated', 'form': form})

        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')
