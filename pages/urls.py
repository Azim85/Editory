from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about_us/', AboutUs.as_view(), name='webinars'),
    path('article/', Articles.as_view(), name='article'),
    path('news/', News.as_view(), name='news'),
]
