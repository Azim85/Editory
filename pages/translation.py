from modeltranslation.translator import translator, TranslationOptions
from .models import Topic, TopResearches, Tariffs


class TopicTranslation(TranslationOptions):
    fields = ('material_name', 'title', 'description', 'others')


class TopResearchTranslation(TranslationOptions):
    fields = ('title', 'author', 'description', 'more')


class TariffsTranslation(TranslationOptions):
    fields = ('text',)


translator.register(Tariffs, TariffsTranslation)
translator.register(Topic, TopicTranslation)
translator.register(TopResearches, TopResearchTranslation)
