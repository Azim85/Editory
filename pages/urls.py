from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('research/', Research.as_view(), name='research'),
    path('research/intelligense/', Research_intelligense.as_view(), name='research_intelligense'),
    path('scientific-papers/', Scientific.as_view(), name='scientific-papers'),
    path('article/', Articles.as_view(), name='article'),
    path('top_researches/', TopResearches.as_view(), name='top-researches'),
    path('webinars/', WebinarsView.as_view(), name='webinars'),
    path('news/', News.as_view(), name='webinars'),
    path('about_us/', About_us.as_view(), name='webinars'),

]
