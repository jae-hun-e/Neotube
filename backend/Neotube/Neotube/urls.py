"""Neotube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

from .views import GuideAPIView, BrowseAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="login/index.html"), name='login'),

    # * Django Third Pary Apps URL
    path('accounts/', include('user.urls')),
    path('api-token-auth/', obtain_auth_token),


    # * Django My Apps URL
    path('guide/', GuideAPIView.as_view(), name='guide'),
    path('browse/', BrowseAPIView.as_view(), name='browse'),
    path('watch/', include('watch.urls')),
    path('comment/', include('comment.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
