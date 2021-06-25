from modeltranslation.translator import translator, TranslationOptions
from .models import Topic, TopResearches


class TopicTranslation(TranslationOptions):
    fields = ('material_name', 'title', 'description', 'others')


class TopResearchTranslation(TranslationOptions):
    fields = ('title', 'author', 'description', 'more')


translator.register(Topic, TopicTranslation)
translator.register(TopResearches, TopResearchTranslation)
