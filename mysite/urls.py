#configure urls here for routing
"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
Add an import:  from my_app import views
Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
Import the include() function: from django.conf.urls import url, include
Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from django import template



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^time$', TemplateView.as_view(template_name="time.html"), name='time'),
]
