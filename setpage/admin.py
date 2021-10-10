from django.contrib import admin

from .models import WebinarsModel, TranslationModel

from .models import (AboutUsModel, ResearchPlatformsContext, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                     DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel,
                     ResearchStrategyModel, top10Uz, top25, top10 ,top5Uz, WebinarsUrls1)

from modeltranslation.admin import TabbedTranslationAdmin


class AboutUsAdmin(TabbedTranslationAdmin):
    list_display = ['text1_en']


class BakAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class ConferencesAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class ContactAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class CreateConferenceAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class DesignAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class GrantsAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class PatentAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class ScopusAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class ProofAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class LangAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


class WebinarsAdmin(TabbedTranslationAdmin):
    list_display = ['text1', 'text2']


class TranslationsAdmin(TabbedTranslationAdmin):
    list_display = ['text1']

# class ResearchStrategyAdmin(TabbedTranslationAdmin):
#     list_display = ['text1']


admin.site.register(AboutUsModel, AboutUsAdmin)

admin.site.register(WebinarsModel, WebinarsAdmin)
admin.site.register(TranslationModel, TranslationsAdmin)

admin.site.register(BakModel, BakAdmin)
admin.site.register(ConferencesModel, ConferencesAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(CreateConferenceModel, CreateConferenceAdmin)
admin.site.register(DesignModel, DesignAdmin)
admin.site.register(GrantsModel, GrantsAdmin)
admin.site.register(PatentModel, PatentAdmin)
admin.site.register(ScopusModel, ScopusAdmin)
admin.site.register(ProofModel, ProofAdmin)
admin.site.register(LangEditModel, LangAdmin)
admin.site.register(ResearchStrategyModel)

admin.site.register(ResearchPlatformsContext)

admin.site.register(top10)
admin.site.register(top10Uz)
admin.site.register(top25)
admin.site.register(top5Uz)
admin.site.register(WebinarsUrls1)
