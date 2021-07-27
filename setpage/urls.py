from django.urls import path
from .views import AboutChangeView, WebinarChangeView, TranslationsChangeView


app_name = 'setpage'

urlpatterns = [
    path('', AboutChangeView.as_view(), name='about-change'),
    path('webinar_change/', WebinarChangeView.as_view(), name='webinar-change'),
    path('translations_change/', TranslationsChangeView.as_view(), name='translations-change')
]
