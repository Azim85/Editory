from django.contrib import admin

from .models import WebinarsModel, TranslationModel

from .models import (AboutUsModel, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                     DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel,
                     ResearchStrategyModel)

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
    list_display = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8']

class ResearchStrategyAdmin(TabbedTranslationAdmin):
    list_display = ['text1']


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
admin.site.register(ResearchStrategyModel, ResearchStrategyAdmin)
