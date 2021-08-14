"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

# Sitemap libraries for search engines
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from pages.sitemaps import StaticViewSitemap, ArticleSitemap
from my_requests.sitemaps import RequestSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'articles': ArticleSitemap,
    'requests': RequestSitemap
}

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('apelsin_pay/', include('apelsinuz.urls')),
    path('paycom/', include('paymeuz.urls')),
    path('', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),  name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/uidb64/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),    
]



urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('request_to/', include('my_requests.urls')),
    path('orders/', include('orders.urls')),
    path('editable/', include('setpage.urls')),
    path('', include('pages.urls')),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
