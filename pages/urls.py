from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about_us/', AboutUs.as_view(), name='webinars'),
    path('article/<int:pk>/', Article.as_view(), name='article'),
    path('news/', Articles.as_view(), name='news'),
    path('services/', Services.as_view(), name='services'),
    path('paper/<int:pk>/', Paper.as_view(), name='paper'),
    path('dissertation/', Dissertation.as_view(), name='dissertation'),
    path('research_strategy/', Research_strategy.as_view(), name='research_strategy'),
    path('language_editing/', Language_editing.as_view(), name='language_editing'),
    path('contact/', Contact.as_view(), name='contact'),
    path('top25/', top25.as_view(), name='top25'),
    path('top2uzb/', top2uzb.as_view(), name='top2uzb'),

]
