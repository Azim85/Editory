from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about_us/', AboutUs.as_view(), name='webinars'),
    path('article/<int:pk>/', Article.as_view(), name='article'),
    path('news/', Articles.as_view(), name='news'),
    path('paper/', Paper.as_view(), name='news'),
]
