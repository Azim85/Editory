from django.shortcuts import render, redirect
from django.views.generic import View
from .models import AboutUsModel, WebinarsModel, TranslationModel


class AboutChangeView(View):

    def post(self, request):
        about_model = AboutUsModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            about_model.text1_en = request.POST.get('text1_en')
            about_model.text1_ru = request.POST.get('text1_ru')
            about_model.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            about_model.text2_en = request.POST.get('text2_en')
            about_model.text2_ru = request.POST.get('text2_ru')
            about_model.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            about_model.text3_en = request.POST.get('text3_en')
            about_model.text3_ru = request.POST.get('text3_ru')
            about_model.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4_en') and request.POST.get('text4_ru') and request.POST.get('text4_uz'):
            about_model.text4_en = request.POST.get('text4_en')
            about_model.text4_ru = request.POST.get('text4_ru')
            about_model.text4_uz = request.POST.get('text4_uz')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            about_model.text5_en = request.POST.get('text5_en')
            about_model.text5_ru = request.POST.get('text5_ru')
            about_model.text5_uz = request.POST.get('text5_uz')
        if request.POST.get('text6_en') and request.POST.get('text6_ru') and request.POST.get('text6_uz'):
            about_model.text6_en = request.POST.get('text6_en')
            about_model.text6_ru = request.POST.get('text6_ru')
            about_model.text6_uz = request.POST.get('text6_uz')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            about_model.text7_en = request.POST.get('text7_en')
            about_model.text7_ru = request.POST.get('text7_ru')
            about_model.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8_en') and request.POST.get('text8_ru') and request.POST.get('text8_uz'):
            about_model.text8_en = request.POST.get('text8_en')
            about_model.text8_ru = request.POST.get('text8_ru')
            about_model.text8_uz = request.POST.get('text8_uz')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            about_model.text9_en = request.POST.get('text9_en')
            about_model.text9_ru = request.POST.get('text9_ru')
            about_model.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            about_model.text10_en = request.POST.get('text10_en')
            about_model.text10_ru = request.POST.get('text10_ru')
            about_model.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            about_model.text11_en = request.POST.get('text11_en')
            about_model.text11_ru = request.POST.get('text11_ru')
            about_model.text11_uz = request.POST.get('text11_uz')

        about_model.save()
        return redirect('pages:webinars')


class WebinarChangeView(View):
    def post(self, request):
        webinar_model = WebinarsModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            webinar_model.text1_en = request.POST.get('text1_en')
            webinar_model.text1_ru = request.POST.get('text1_ru')
            webinar_model.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            webinar_model.text2_en = request.POST.get('text2_en')
            webinar_model.text2_ru = request.POST.get('text2_ru')
            webinar_model.text2_uz = request.POST.get('text2_uz')
        webinar_model.save()
        return redirect('requests:webinars')


class TranslationsChangeView(View):
    def post(self, request):
        translations = TranslationModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            translations.text1_en = request.POST.get('text1_en')
            translations.text1_ru = request.POST.get('text1_ru')
            translations.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            translations.text2_en = request.POST.get('text2_en')
            translations.text2_ru = request.POST.get('text2_ru')
            translations.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            translations.text3_en = request.POST.get('text3_en')
            translations.text3_ru = request.POST.get('text3_ru')
            translations.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4_en') and request.POST.get('text4_ru') and request.POST.get('text4_uz'):
            translations.text4_en = request.POST.get('text4_en')
            translations.text4_ru = request.POST.get('text4_ru')
            translations.text4_uz = request.POST.get('text4_uz')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            translations.text5_en = request.POST.get('text5_en')
            translations.text5_ru = request.POST.get('text5_ru')
            translations.text5_uz = request.POST.get('text5_uz')
        if request.POST.get('text6_en') and request.POST.get('text6_ru') and request.POST.get('text6_uz'):
            translations.text6_en = request.POST.get('text6_en')
            translations.text6_ru = request.POST.get('text6_ru')
            translations.text6_uz = request.POST.get('text6_uz')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            translations.text7_en = request.POST.get('text7_en')
            translations.text7_ru = request.POST.get('text7_ru')
            translations.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8_en') and request.POST.get('text8_ru') and request.POST.get('text8_uz'):
            translations.text8_en = request.POST.get('text8_en')
            translations.text8_ru = request.POST.get('text8_ru')
            translations.text8_uz = request.POST.get('text8_uz')
        translations.save()
        return redirect('requests:translation')
