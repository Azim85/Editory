from django.urls import path
from .views import (Research, ResearchIntelligense, Scientific, Peer_review,
                    TopResearchess, WebinarsView, Conferences,
                     ConsultationView, FreeConsultationView, Proofreading,
                     BAKView, ScopusView, GrantsView, PatentsView)
                     
app_name = 'requests'

urlpatterns = [
    path('research/', Research.as_view(), name='research'),
    path('research/intelligense/', ResearchIntelligense.as_view(),
         name='research_intelligense'),
    path('scientific-papers/', Scientific.as_view(), name='scientific-papers'),
    path('top_researches/', TopResearchess.as_view(), name='top-researches'),
    path('webinars/', WebinarsView.as_view(), name='webinars'),
    path('conferences/', Conferences.as_view(), name='conferences'),
    path('consultation/', ConsultationView.as_view(), name='consultation'),
    path('free_consultation/', FreeConsultationView.as_view(), name='free_consultation'),
    path('proofreading/', Proofreading.as_view(), name='proofreading'),
    path('peer_review/', Peer_review.as_view(), name='peer_review'),

    path('bak/', BAKView.as_view(), name='bak'),
    path('scopus/', ScopusView.as_view(), name='scopus'),
    path('grants/', GrantsView.as_view(), name='grants'),
    path('patents/', PatentsView.as_view(), name='patents')
]
