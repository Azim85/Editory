from django.urls import path
from .views import HomeView, Research

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('research/', Research.as_view(), name='research')
]
