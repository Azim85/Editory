from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, View
from pages.models import TopResearches
from .forms import (ConsultationForm, FreeConsultationForm, ProofreadingForm,
                    PeerReviewForm, OrganizeConferencesForm, GrantsForm, TranslationForm)
from .models import Translation


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

# todo yangilash
class Conferences(View):
    def get(self, request):
        context = {'form': FreeConsultationForm()}
        return render(request, 'conferences.html', context)

    def post(self, request):
        print(request.POST)


class CreateConferences(View):
    def get(self, request):
        context = {'form': OrganizeConferencesForm()}
        return render(request, 'creat_conference.html', context)

    def post(self, request):
        form = OrganizeConferencesForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('pages:home')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'home.html', {'validated':'validated', 'form':form})            
            else:    
                return render(request,'home.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')



class Design(View):
    def get(self, request):
        context = {'form': GrantsForm()}
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
                    return render(request,'design.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'design.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')
        



class ConsultationView(View):
    def post(self, request):
        form = ConsultationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                if request.POST.get('is_agree') and request.POST.get('is_agree') == 'on':
                    done = form.save()
                    if done:
                        messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                        return redirect('pages:home')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'home.html', {'validated':'validated', 'form':form})            
            else:    
                return render(request,'home.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

class FreeConsultationView(View):
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
                    return render(request,'conferences.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'conferences.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class Proofreading(View):
    def get(self, request):
        context = {'form': ProofreadingForm()}
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
            return render(request, 'proofreading.html', {'form':form})
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
            return render(request, 'peer_review.html', {'form':form})
        else:    
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')


class BAKView(View):
    def get(self, request):
        form = GrantsForm()
        return render(request, 'bak.html', {'form':form})

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
                        return redirect('requests:bak')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'bak.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'bak.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

    


class ScopusView(View):
    def get(self, request):
        form = GrantsForm()
        return render(request, 'scopus.html', {'form':form})

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
                        return redirect('requests:scopus')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'scopus.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'scopus.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

class GrantsView(View):
    def get(self, request):
        form = GrantsForm()
        return render(request, 'grants.html', {'form':form})

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
                        return redirect('requests:grants')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'grants.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'grants.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

class PatentsView(View):
    def get(self, request):
        form = GrantsForm()
        return render(request, 'patents.html', {'form':form})

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
                        return redirect('requests:patents')
                else:
                    messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                    return render(request,'patents.html', {'validated':'validated', 'form':form})
            else:    
                return render(request,'patents.html', {'validated':'validated', 'form':form})
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')

class TranslationView(View):
    def get(self, request):
        form = TranslationForm()
        return render(request, 'translation.html', {'form':form})

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
                 research_area=research_area, extra=extra, comment=comment, file=file, is_agree=is_agree)
                if done:
                    messages.success(request, 'Ваш запрос успешно отправлен, мы скоро свяжемся с вами!')
                    return redirect('requests:translation')
            else:
                messages.error(request, 'вы  должны согласиться прежде чем отправить форму ')
                return render(request,'translation.html', {'validated':'validated', 'form':form})
            
        else:
            messages.error(request, 'Чтобы отправить форму, вы должны сначала войти в систему')
            return redirect('users:login')