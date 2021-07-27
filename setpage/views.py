from django.shortcuts import render, redirect
from django.views.generic import View
from .models import (AboutUsModel, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                        DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel)

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


class BakChangeView(View):
    def post(self, request):
        bak_model = BakModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            bak_model.text1_en = request.POST.get('text1_en')
            bak_model.text1_ru = request.POST.get('text1_ru')
            bak_model.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            bak_model.text2_en = request.POST.get('text2_en')
            bak_model.text2_ru = request.POST.get('text2_ru')
            bak_model.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            bak_model.text3_en = request.POST.get('text3_en')
            bak_model.text3_ru = request.POST.get('text3_ru')
            bak_model.text3_uz = request.POST.get('text3_uz')
        if request.FILES.get('text4'):
            bak_model.text4 = request.FILES.get('text4')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            bak_model.text5_en = request.POST.get('text5_en')
            bak_model.text5_ru = request.POST.get('text5_ru')
            bak_model.text5_uz = request.POST.get('text5_uz')
        if request.FILES.get('text6'):
            bak_model.text6 = request.FILES.get('text6')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            bak_model.text7_en = request.POST.get('text7_en')
            bak_model.text7_ru = request.POST.get('text7_ru')
            bak_model.text7_uz = request.POST.get('text7_uz')
        if request.FILES.get('text8'):
            bak_model.text8 = request.FILES.get('text8')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            bak_model.text9_en = request.POST.get('text9_en')
            bak_model.text9_ru = request.POST.get('text9_ru')
            bak_model.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            bak_model.text10_en = request.POST.get('text10_en')
            bak_model.text10_ru = request.POST.get('text10_ru')
            bak_model.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            bak_model.text11_en = request.POST.get('text11_en')
            bak_model.text11_ru = request.POST.get('text11_ru')
            bak_model.text11_uz = request.POST.get('text11_uz')
        if request.POST.get('text12_en') and request.POST.get('text12_ru') and request.POST.get('text12_uz'):
            bak_model.text12_en = request.POST.get('text12_en')
            bak_model.text12_ru = request.POST.get('text12_ru')
            bak_model.text12_uz = request.POST.get('text12_uz')
        if request.POST.get('text13_en') and request.POST.get('text13_ru') and request.POST.get('text13_uz'):
            bak_model.text13_en = request.POST.get('text13_en')
            bak_model.text13_ru = request.POST.get('text13_ru')
            bak_model.text13_uz = request.POST.get('text13_uz')
        if request.POST.get('text14_en') and request.POST.get('text14_ru') and request.POST.get('text14_uz'):
            bak_model.text14_en = request.POST.get('text14_en')
            bak_model.text14_ru = request.POST.get('text14_ru')
            bak_model.text14_uz = request.POST.get('text14_uz')
        if request.POST.get('text15_en') and request.POST.get('text15_ru') and request.POST.get('text15_uz'):
            bak_model.text15_en = request.POST.get('text15_en')
            bak_model.text15_ru = request.POST.get('text15_ru')
            bak_model.text15_uz = request.POST.get('text15_uz')
        if request.POST.get('text16_en') and request.POST.get('text16_ru') and request.POST.get('text16_uz'):
            bak_model.text16_en = request.POST.get('text16_en')
            bak_model.text16_ru = request.POST.get('text16_ru')
            bak_model.text16_uz = request.POST.get('text16_uz')

        bak_model.save()
        return redirect('requests:bak')



class ConferencesChangeView(View):
    def post(self, request):
        con_model = ConferencesModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            con_model.text1_en = request.POST.get('text1_en')
            con_model.text1_ru = request.POST.get('text1_ru')
            con_model.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            con_model.text2_en = request.POST.get('text2_en')
            con_model.text2_ru = request.POST.get('text2_ru')
            con_model.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            con_model.text3_en = request.POST.get('text3_en')
            con_model.text3_ru = request.POST.get('text3_ru')
            con_model.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4') and request.POST.get('text4_link'):
            con_model.text4 = request.POST.get('text4')
            con_model.text4_link = request.POST.get('text4_link')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            con_model.text5_en = request.POST.get('text5_en')
            con_model.text5_ru = request.POST.get('text5_ru')
            con_model.text5_uz = request.POST.get('text5_uz')  
        if request.POST.get('text6') and request.POST.get('text6_link'):
            con_model.text6 = request.POST.get('text6')
            con_model.text6_link = request.POST.get('text6_link')  
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            con_model.text7_en = request.POST.get('text7_en')
            con_model.text7_ru = request.POST.get('text7_ru')
            con_model.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8') and request.POST.get('text8_link'):
            con_model.text8 = request.POST.get('text8')
            con_model.text8_link = request.POST.get('text8_link')  
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            con_model.text9_en = request.POST.get('text9_en')
            con_model.text9_ru = request.POST.get('text9_ru')
            con_model.text9_uz = request.POST.get('text9_uz') 
        if request.POST.get('text10') and request.POST.get('text10_link'):
            con_model.text10 = request.POST.get('text10')
            con_model.text10_link = request.POST.get('text10_link')  
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            con_model.text11_en = request.POST.get('text11_en')
            con_model.text11_ru = request.POST.get('text11_ru')
            con_model.text11_uz = request.POST.get('text11_uz')
        if request.POST.get('text12') and request.POST.get('text12_link'):
            con_model.text12 = request.POST.get('text12')
            con_model.text12_link = request.POST.get('text12_link')  
        if request.POST.get('text13_en') and request.POST.get('text13_ru') and request.POST.get('text13_uz'):
            con_model.text13_en = request.POST.get('text13_en')
            con_model.text13_ru = request.POST.get('text13_ru')
            con_model.text13_uz = request.POST.get('text13_uz')
        if request.POST.get('text14') and request.POST.get('text14_link'):
            con_model.text14 = request.POST.get('text14')
            con_model.text14_link = request.POST.get('text14_link')  
        if request.POST.get('text15_en') and request.POST.get('text15_ru') and request.POST.get('text15_uz'):
            con_model.text15_en = request.POST.get('text15_en')
            con_model.text15_ru = request.POST.get('text15_ru')
            con_model.text15_uz = request.POST.get('text15_uz')
        if request.POST.get('text16_en') and request.POST.get('text16_ru') and request.POST.get('text16_uz'):
            con_model.text16_en = request.POST.get('text16_en')
            con_model.text16_ru = request.POST.get('text16_ru')
            con_model.text16_uz = request.POST.get('text16_uz')
        if request.POST.get('text17_en') and request.POST.get('text17_ru') and request.POST.get('text17_uz'):
            con_model.text17_en = request.POST.get('text17_en')
            con_model.text17_ru = request.POST.get('text17_ru')
            con_model.text17_uz = request.POST.get('text17_uz') 
            
        
        con_model.save()
        return redirect('requests:conferences')


class ContactChangeView(View):
    def post(self, request):
        contact_model = ContactModel.objects.first()
        if request.POST.get('text1'):
            contact_model.text1 = request.POST.get('text1')
        if request.POST.get('text2'):
            contact_model.text2 = request.POST.get('text2')
        if request.POST.get('text3'):
            contact_model.text3 = request.POST.get('text3')
        if request.POST.get('text4'):
            contact_model.text4 = request.POST.get('text4')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            contact_model.text5_en = request.POST.get('text5_en')
            contact_model.text5_ru = request.POST.get('text5_ru')
            contact_model.text5_uz = request.POST.get('text5_uz') 
             


        contact_model.save()
        return redirect('pages:contact')


class CreateConferenceChangeView(View):
    def post(self, request):
        obj = CreateConferenceModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz') 

        obj.save()
        return redirect('requests:creat-conferences')
from django.views.decorators.csrf import csrf_exempt


class DesignChangeView(View):
    @csrf_exempt
    def post(self, request):
        obj = DesignModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')
        if request.FILES.get('text3'):
            obj.text3 = request.FILES.get('text3')
        if request.POST.get('text4_en') and request.POST.get('text4_ru') and request.POST.get('text4_uz'):
            obj.text4_en = request.POST.get('text4_en')
            obj.text4_ru = request.POST.get('text4_ru')
            obj.text4_uz = request.POST.get('text4_uz')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            obj.text5_en = request.POST.get('text5_en')
            obj.text5_ru = request.POST.get('text5_ru')
            obj.text5_uz = request.POST.get('text5_uz')
        if request.FILES.get('text6'):
            obj.text6 = request.FILES.get('text6')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            obj.text7_en = request.POST.get('text7_en')
            obj.text7_ru = request.POST.get('text7_ru')
            obj.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8_en') and request.POST.get('text8_ru') and request.POST.get('text8_uz'):
            obj.text8_en = request.POST.get('text8_en')
            obj.text8_ru = request.POST.get('text8_ru')
            obj.text8_uz = request.POST.get('text8_uz')
        if request.FILES.get('text9'):
            obj.text9 = request.FILES.get('text9')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            obj.text10_en = request.POST.get('text10_en')
            obj.text10_ru = request.POST.get('text10_ru')
            obj.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            obj.text11_en = request.POST.get('text11_en')
            obj.text11_ru = request.POST.get('text11_ru')
            obj.text11_uz = request.POST.get('text11_uz')

        obj.save()
        return redirect('requests:design')


class GrantChangeView(View):
    def post(self, request):
        obj = GrantsModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')

        obj.save()
        return redirect('requests:grants')


class PatentChangeView(View):
    def post(self, request):
        obj = PatentModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            obj.text3_en = request.POST.get('text3_en')
            obj.text3_ru = request.POST.get('text3_ru')
            obj.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4_en') and request.POST.get('text4_ru') and request.POST.get('text4_uz'):
            obj.text4_en = request.POST.get('text4_en')
            obj.text4_ru = request.POST.get('text4_ru')
            obj.text4_uz = request.POST.get('text4_uz')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            obj.text5_en = request.POST.get('text5_en')
            obj.text5_ru = request.POST.get('text5_ru')
            obj.text5_uz = request.POST.get('text5_uz')
        if request.POST.get('text6_en') and request.POST.get('text6_ru') and request.POST.get('text6_uz'):
            obj.text6_en = request.POST.get('text6_en')
            obj.text6_ru = request.POST.get('text6_ru')
            obj.text6_uz = request.POST.get('text6_uz')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            obj.text7_en = request.POST.get('text7_en')
            obj.text7_ru = request.POST.get('text7_ru')
            obj.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8_en') and request.POST.get('text8_ru') and request.POST.get('text8_uz'):
            obj.text8_en = request.POST.get('text8_en')
            obj.text8_ru = request.POST.get('text8_ru')
            obj.text8_uz = request.POST.get('text8_uz')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            obj.text9_en = request.POST.get('text9_en')
            obj.text9_ru = request.POST.get('text9_ru')
            obj.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            obj.text10_en = request.POST.get('text10_en')
            obj.text10_ru = request.POST.get('text10_ru')
            obj.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            obj.text11_en = request.POST.get('text11_en')
            obj.text11_ru = request.POST.get('text11_ru')
            obj.text11_uz = request.POST.get('text11_uz')


        obj.save()
        return redirect('requests:patents')


class ScopusChangeView(View):
    def post(self, request):
        obj = ScopusModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')
        if request.FILES.get('text3'):
            obj.text3 = request.FILES.get('text3')
        if request.FILES.get('text4'):
            obj.text4 = request.FILES.get('text4')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            obj.text5_en = request.POST.get('text5_en')
            obj.text5_ru = request.POST.get('text5_ru')
            obj.text5_uz = request.POST.get('text5_uz')
        if request.FILES.get('text6'):
            obj.text6 = request.FILES.get('text6')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            obj.text7_en = request.POST.get('text7_en')
            obj.text7_ru = request.POST.get('text7_ru')
            obj.text7_uz = request.POST.get('text7_uz')
        if request.FILES.get('text8'):
            obj.text8 = request.FILES.get('text8')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            obj.text9_en = request.POST.get('text9_en')
            obj.text9_ru = request.POST.get('text9_ru')
            obj.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            obj.text10_en = request.POST.get('text10_en')
            obj.text10_ru = request.POST.get('text10_ru')
            obj.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            obj.text11_en = request.POST.get('text11_en')
            obj.text11_ru = request.POST.get('text11_ru')
            obj.text11_uz = request.POST.get('text11_uz')
        if request.POST.get('text12_en') and request.POST.get('text12_ru') and request.POST.get('text12_uz'):
            obj.text12_en = request.POST.get('text12_en')
            obj.text12_ru = request.POST.get('text12_ru')
            obj.text12_uz = request.POST.get('text12_uz')
        if request.POST.get('text13_en') and request.POST.get('text13_ru') and request.POST.get('text13_uz'):
            obj.text13_en = request.POST.get('text13_en')
            obj.text13_ru = request.POST.get('text13_ru')
            obj.text13_uz = request.POST.get('text13_uz')
        if request.POST.get('text14_en') and request.POST.get('text14_ru') and request.POST.get('text14_uz'):
            obj.text14_en = request.POST.get('text14_en')
            obj.text14_ru = request.POST.get('text14_ru')
            obj.text14_uz = request.POST.get('text14_uz')
        if request.POST.get('text15_en') and request.POST.get('text15_ru') and request.POST.get('text15_uz'):
            obj.text15_en = request.POST.get('text15_en')
            obj.text15_ru = request.POST.get('text15_ru')
            obj.text15_uz = request.POST.get('text15_uz')
        if request.POST.get('text16_en') and request.POST.get('text16_ru') and request.POST.get('text16_uz'):
            obj.text16_en = request.POST.get('text16_en')
            obj.text16_ru = request.POST.get('text16_ru')
            obj.text16_uz = request.POST.get('text16_uz')      


        obj.save()
        return redirect('requests:scopus')


class ProofChangeView(View):
    def post(self, request):
        obj = ProofModel.objects.first()
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            obj.text3_en = request.POST.get('text3_en')
            obj.text3_ru = request.POST.get('text3_ru')
            obj.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4_en') and request.POST.get('text4_ru') and request.POST.get('text4_uz'):
            obj.text4_en = request.POST.get('text4_en')
            obj.text4_ru = request.POST.get('text4_ru')
            obj.text4_uz = request.POST.get('text4_uz')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            obj.text5_en = request.POST.get('text5_en')
            obj.text5_ru = request.POST.get('text5_ru')
            obj.text5_uz = request.POST.get('text5_uz')
        if request.POST.get('text6_en') and request.POST.get('text6_ru') and request.POST.get('text6_uz'):
            obj.text6_en = request.POST.get('text6_en')
            obj.text6_ru = request.POST.get('text6_ru')
            obj.text6_uz = request.POST.get('text6_uz')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            obj.text7_en = request.POST.get('text7_en')
            obj.text7_ru = request.POST.get('text7_ru')
            obj.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8_en') and request.POST.get('text8_ru') and request.POST.get('text8_uz'):
            obj.text8_en = request.POST.get('text8_en')
            obj.text8_ru = request.POST.get('text8_ru')
            obj.text8_uz = request.POST.get('text8_uz')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            obj.text9_en = request.POST.get('text9_en')
            obj.text9_ru = request.POST.get('text9_ru')
            obj.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            obj.text10_en = request.POST.get('text10_en')
            obj.text10_ru = request.POST.get('text10_ru')
            obj.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            obj.text11_en = request.POST.get('text11_en')
            obj.text11_ru = request.POST.get('text11_ru')
            obj.text11_uz = request.POST.get('text11_uz')
        if request.POST.get('text12_en') and request.POST.get('text12_ru') and request.POST.get('text12_uz'):
            obj.text12_en = request.POST.get('text12_en')
            obj.text12_ru = request.POST.get('text12_ru')
            obj.text12_uz = request.POST.get('text12_uz')
        if request.POST.get('text13_en') and request.POST.get('text13_ru') and request.POST.get('text13_uz'):
            obj.text13_en = request.POST.get('text13_en')
            obj.text13_ru = request.POST.get('text13_ru')
            obj.text13_uz = request.POST.get('text13_uz')

        obj.save()
        return redirect('requests:proofreading')


class LangChangeView(View):
    def post(self, request):
        obj = LangEditModel.objects.first()
        if request.POST.get('text25_en') and request.POST.get('text25_ru') and request.POST.get('text25_uz'):
            obj.text25_en = request.POST.get('text25_en')
            obj.text25_ru = request.POST.get('text25_ru')
            obj.text25_uz = request.POST.get('text25_uz')
        if request.POST.get('text1_en') and request.POST.get('text1_ru') and request.POST.get('text1_uz'):
            obj.text1_en = request.POST.get('text1_en')
            obj.text1_ru = request.POST.get('text1_ru')
            obj.text1_uz = request.POST.get('text1_uz')
        if request.POST.get('text2_en') and request.POST.get('text2_ru') and request.POST.get('text2_uz'):
            obj.text2_en = request.POST.get('text2_en')
            obj.text2_ru = request.POST.get('text2_ru')
            obj.text2_uz = request.POST.get('text2_uz')
        if request.POST.get('text3_en') and request.POST.get('text3_ru') and request.POST.get('text3_uz'):
            obj.text3_en = request.POST.get('text3_en')
            obj.text3_ru = request.POST.get('text3_ru')
            obj.text3_uz = request.POST.get('text3_uz')
        if request.POST.get('text4'):
            obj.text4 = request.POST.get('text4')
        if request.POST.get('text5_en') and request.POST.get('text5_ru') and request.POST.get('text5_uz'):
            obj.text5_en = request.POST.get('text5_en')
            obj.text5_ru = request.POST.get('text5_ru')
            obj.text5_uz = request.POST.get('text5_uz')
        if request.POST.get('text6'):
            obj.text6 = request.POST.get('text6')
        if request.POST.get('text7_en') and request.POST.get('text7_ru') and request.POST.get('text7_uz'):
            obj.text7_en = request.POST.get('text7_en')
            obj.text7_ru = request.POST.get('text7_ru')
            obj.text7_uz = request.POST.get('text7_uz')
        if request.POST.get('text8'):
            obj.text8 = request.POST.get('text8')
        if request.POST.get('text9_en') and request.POST.get('text9_ru') and request.POST.get('text9_uz'):
            obj.text9_en = request.POST.get('text9_en')
            obj.text9_ru = request.POST.get('text9_ru')
            obj.text9_uz = request.POST.get('text9_uz')
        if request.POST.get('text10_en') and request.POST.get('text10_ru') and request.POST.get('text10_uz'):
            obj.text10_en = request.POST.get('text10_en')
            obj.text10_ru = request.POST.get('text10_ru')
            obj.text10_uz = request.POST.get('text10_uz')
        if request.POST.get('text11_en') and request.POST.get('text11_ru') and request.POST.get('text11_uz'):
            obj.text11_en = request.POST.get('text11_en')
            obj.text11_ru = request.POST.get('text11_ru')
            obj.text11_uz = request.POST.get('text11_uz')
        if request.POST.get('text12_en') and request.POST.get('text12_ru') and request.POST.get('text12_uz'):
            obj.text12_en = request.POST.get('text12_en')
            obj.text12_ru = request.POST.get('text12_ru')
            obj.text12_uz = request.POST.get('text12_uz')
        if request.POST.get('text13_en') and request.POST.get('text13_ru') and request.POST.get('text13_uz'):
            obj.text13_en = request.POST.get('text13_en')
            obj.text13_ru = request.POST.get('text13_ru')
            obj.text13_uz = request.POST.get('text13_uz')
        if request.POST.get('text14_en') and request.POST.get('text14_ru') and request.POST.get('text14_uz'):
            obj.text14_en = request.POST.get('text14_en')
            obj.text14_ru = request.POST.get('text14_ru')
            obj.text14_uz = request.POST.get('text14_uz')
        if request.POST.get('text15_en') and request.POST.get('text15_ru') and request.POST.get('text15_uz'):
            obj.text15_en = request.POST.get('text15_en')
            obj.text15_ru = request.POST.get('text15_ru')
            obj.text15_uz = request.POST.get('text15_uz')
        if request.POST.get('text16_en') and request.POST.get('text16_ru') and request.POST.get('text16_uz'):
            obj.text16_en = request.POST.get('text16_en')
            obj.text16_ru = request.POST.get('text16_ru')
            obj.text16_uz = request.POST.get('text16_uz')
        if request.POST.get('text17_en') and request.POST.get('text17_ru') and request.POST.get('text17_uz'):
            obj.text17_en = request.POST.get('text17_en')
            obj.text17_ru = request.POST.get('text17_ru')
            obj.text17_uz = request.POST.get('text17_uz')
        if request.POST.get('text18_en') and request.POST.get('text18_ru') and request.POST.get('text18_uz'):
            obj.text18_en = request.POST.get('text18_en')
            obj.text18_ru = request.POST.get('text18_ru')
            obj.text18_uz = request.POST.get('text18_uz')
        if request.POST.get('text19_en') and request.POST.get('text19_ru') and request.POST.get('text19_uz'):
            obj.text19_en = request.POST.get('text19_en')
            obj.text19_ru = request.POST.get('text19_ru')
            obj.text19_uz = request.POST.get('text19_uz')
        if request.POST.get('text20_en') and request.POST.get('text20_ru') and request.POST.get('text20_uz'):
            obj.text20_en = request.POST.get('text20_en')
            obj.text20_ru = request.POST.get('text20_ru')
            obj.text20_uz = request.POST.get('text20_uz')
        if request.POST.get('text21_en') and request.POST.get('text21_ru') and request.POST.get('text21_uz'):
            obj.text21_en = request.POST.get('text21_en')
            obj.text21_ru = request.POST.get('text21_ru')
            obj.text21_uz = request.POST.get('text21_uz')
        if request.POST.get('text22_en') and request.POST.get('text22_ru') and request.POST.get('text22_uz'):
            obj.text22_en = request.POST.get('text22_en')
            obj.text22_ru = request.POST.get('text22_ru')
            obj.text22_uz = request.POST.get('text22_uz')
        if request.POST.get('text23_en') and request.POST.get('text23_ru') and request.POST.get('text23_uz'):
            obj.text23_en = request.POST.get('text23_en')
            obj.text23_ru = request.POST.get('text23_ru')
            obj.text23_uz = request.POST.get('text23_uz')
        if request.POST.get('text24_en') and request.POST.get('text24_ru') and request.POST.get('text24_uz'):
            obj.text24_en = request.POST.get('text24_en')
            obj.text24_ru = request.POST.get('text24_ru')
            obj.text24_uz = request.POST.get('text24_uz')


        obj.save()
        return redirect('pages:language_editing')






