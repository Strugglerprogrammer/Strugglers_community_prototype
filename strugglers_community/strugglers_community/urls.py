"""
URL configuration for strugglers_community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import logging

logger = logging.getLogger(__name__)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # Community space app
    path('education/', include('education.urls', namespace='education')),
    path('finance/', include('finance.urls', namespace='finance')),
    path('lifestyle/', include('lifestyle.urls', namespace='lifestyle')),
    path('career/', include('career.urls', namespace='career')),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

logger.info(f"URL Patterns: {urlpatterns}")