from django.contrib import admin
from .models import AboutUsModel, WebinarsModel, TranslationModel
from modeltranslation.admin import TabbedTranslationAdmin


class AboutUsAdmin(TabbedTranslationAdmin):
    list_display = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11']


class WebinarsAdmin(TabbedTranslationAdmin):
    list_display = ['text1', 'text2']


class TranslationsAdmin(TabbedTranslationAdmin):
    list_display = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8']


admin.site.register(AboutUsModel, AboutUsAdmin)
admin.site.register(WebinarsModel, WebinarsAdmin)
admin.site.register(TranslationModel, TranslationsAdmin)
