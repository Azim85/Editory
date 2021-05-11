from django.urls import path
from .views import (Research, ResearchIntelligense, Scientific, TopResearchess, WebinarsView, Conferences)

app_name = 'requests'

urlpatterns = [
    path('research/', Research.as_view(), name='research'),
    path('research/intelligense/', ResearchIntelligense.as_view(), name='research_intelligense'),
    path('scientific-papers/', Scientific.as_view(), name='scientific-papers'),
    path('top_researches/', TopResearchess.as_view(), name='top-researches'),
    path('webinars/', WebinarsView.as_view(), name='webinars'),
    path('conferences/', Conferences.as_view(), name='conferences'),
]