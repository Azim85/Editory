from django.urls import path
from .views import ( AboutChangeView, BakChangeView, ConferencesChangeView, ContactChangeView, CreateConferenceChangeView,
                    DesignChangeView, GrantChangeView, PatentChangeView, ScopusChangeView, ProofChangeView, LangChangeView,
                     WebinarChangeView, TranslationsChangeView)



app_name = 'setpage'

urlpatterns = [
    path('', AboutChangeView.as_view(), name='about-change'),

    path('webinar_change/', WebinarChangeView.as_view(), name='webinar-change'),
    path('translations_change/', TranslationsChangeView.as_view(), name='translations-change'),


    path('bak_change/', BakChangeView.as_view(), name='bak-change'),
    path('conferences_change/', ConferencesChangeView.as_view(), name='con-change'),
    path('contact_change/', ContactChangeView.as_view(), name='contact-change'),
    path('create_conference_change/', CreateConferenceChangeView.as_view(), name='conference-change'),
    path('design_change/', DesignChangeView.as_view(), name='design-change'),
    path('grant_change/', GrantChangeView.as_view(), name='grant-change'),
    path('patent_change/', PatentChangeView.as_view(), name='patent-change'),
    path('scopus_change/', ScopusChangeView.as_view(), name='scopus-change'),
    path('proof_change/', ProofChangeView.as_view(), name='proof-change'),
    path('lang_change/', LangChangeView.as_view(), name='lang-change'),

]
