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
    path('research_strategy/',  Research_strategy.as_view(), name='research_strategy'),
    path('language_editing/', Language_editing.as_view(), name='language_editing'),
    path('contact/', Contact.as_view(), name='contact'),
    path('top25/', top25v, name='top25'),
    path('top2uzb/', top2uzb, name='top2uzb'),
    path('top10/', top10one, name='top10'),
    path('top10uz/', top10uz, name='top10uz'),
    path('all_news/', allNews.as_view(), name="allnews"),

    path('change_image', change_image, name="image-change"),
    path('change_material', change_material, name="material-change"),
    path('change_title', change_title, name="title-change"),
    path('change_others', change_others, name='others-change'),
    path('change_description', change_description, name="description-change"),

    path('search/', SearchView.as_view(), name='search'),
    path('all_webinars/', all_webinars, name='all-webinars')

]
