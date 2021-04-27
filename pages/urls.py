from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('research/', Research.as_view(), name='research'),
    path('research/intelligense/', Research_intelligense.as_view(), name='research_intelligense'),
    path('scientific-papers/', Scientific.as_view(), name='scientific-papers')

]
