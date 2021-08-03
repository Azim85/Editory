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

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('apelsin_pay/', include('apelsinuz.urls')),
    path('paycom/', include('paymeuz.urls')),
    path('editorypress/', include('editory_press.urls')),
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
