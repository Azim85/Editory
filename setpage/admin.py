from django.contrib import admin
from .models import ( AboutUsModel, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                        DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel )
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



admin.site.register(AboutUsModel, AboutUsAdmin)
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
