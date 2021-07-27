from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUsModel, WebinarsModel, TranslationModel


class AboutUsTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11')


class WebinarTranslations(TranslationOptions):
    fields = ('text1', 'text2')


class TramslationsTranslations(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8')


translator.register(AboutUsModel, AboutUsTranslation)
translator.register(WebinarsModel, WebinarTranslations)
translator.register(TranslationModel, TramslationsTranslations)
