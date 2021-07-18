from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUsModel



class AboutUsTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11')



translator.register(AboutUsModel, AboutUsTranslation)


