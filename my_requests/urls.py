from django.urls import path
from .views import (Research, ResearchIntelligense, Scientific, Peer_review,
                    ConsultationView, Proofreading, CreateConferences,
                    TopResearchess, WebinarsView, Conferences, Design,
                    BAKView, ScopusView, GrantsView, PatentsView, TranslationView, after_login)

                     
app_name = 'requests'

urlpatterns = [
    path('research/', Research.as_view(), name='research'),
    path('research/intelligense/', ResearchIntelligense.as_view(),
         name='research_intelligense'),
    path('scientific-papers/', Scientific.as_view(), name='scientific-papers'),
    path('top_researches/', TopResearchess.as_view(), name='top-researches'),
    path('webinars/', WebinarsView.as_view(), name='webinars'),
    path('conferences/', Conferences.as_view(), name='conferences'),
    path('creat_conferences/', CreateConferences.as_view(), name='creat-conferences'),
    path('consultation/', ConsultationView.as_view(), name='consultation'),
    # path('free_consultation/', FreeConsultationView.as_view(), name='free_consultation'),
    path('proofreading/', Proofreading.as_view(), name='proofreading'),
    path('peer_review/', Peer_review.as_view(), name='peer_review'),
    path('bak/', BAKView.as_view(), name='bak'),
    path('scopus/', ScopusView.as_view(), name='scopus'),
    path('grants/', GrantsView.as_view(), name='grants'),
    path('patents/', PatentsView.as_view(), name='patents'),
    path('translation/', TranslationView.as_view(), name='translation'),
    path('design/', Design.as_view(), name='design'),

    path('after_login/', after_login, name='after-login')


]
