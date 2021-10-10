from modeltranslation.translator import translator, TranslationOptions
from .models import WebinarsModel, TranslationModel, top5Uz
from .models import (AboutUsModel, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                     DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel,
                     ResearchStrategyModel, top10Uz, top25, top10, ResearchPlatformsContext)


class ResearchPlatformsContextTranslation(TranslationOptions):
    fields = ('context',)

class AboutUsTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9')


class BakTranslation(TranslationOptions):
    fields = (
    'text1', 'text2', 'text3', 'text5', 'text7', 'text9', 'text10', 'text11')


class ConferencesTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5')


class ContactTranslation(TranslationOptions):
    fields = ('text5',)


class CreateConferenceTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4')


class DesignTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text4', 'text5', 'text7', 'text8', 'text10', 'text11')


class GrantsTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4')


class PatentTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4')


class ScopusTranslation(TranslationOptions):
    fields = (
    'text1', 'text2', 'text5', 'text7', 'text9', 'text10', 'text11')


class ProofTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9')


class LangTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5',  'text9')


class WebinarTranslations(TranslationOptions):
    fields = ('text1', 'text2')


class ResearchStrategyTranslations(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9')


class top10UzTranslations(TranslationOptions):
    fields = ('name', 'description')


class top10Translations(TranslationOptions):
    fields = ('name', 'description')


class top25Translations(TranslationOptions):
    fields = ('name', 'description')


class top5UzTranslations(TranslationOptions):
    fields = ('name', 'description')


translator.register(ResearchPlatformsContext, ResearchPlatformsContextTranslation)
translator.register(AboutUsModel, AboutUsTranslation)
translator.register(BakModel, BakTranslation)
translator.register(ConferencesModel, ConferencesTranslation)
translator.register(ContactModel, ContactTranslation)
translator.register(CreateConferenceModel, CreateConferenceTranslation)
translator.register(DesignModel, DesignTranslation)
translator.register(GrantsModel, GrantsTranslation)
translator.register(PatentModel, PatentTranslation)
translator.register(ScopusModel, ScopusTranslation)
translator.register(ProofModel, ProofTranslation)
translator.register(LangEditModel, LangTranslation)
translator.register(ResearchStrategyModel, ResearchStrategyTranslations)


class TramslationsTranslations(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5')


# translator.register(AboutUsModel, AboutUsTranslation)
translator.register(WebinarsModel, WebinarTranslations)
translator.register(TranslationModel, TramslationsTranslations)
translator.register(top10Uz, top10UzTranslations)
translator.register(top25, top25Translations)
translator.register(top5Uz, top5UzTranslations)
translator.register(top10, top10Translations)
