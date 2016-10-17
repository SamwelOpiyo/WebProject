from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^book', views.home, name='book'),
    url(r'^former/', views.former, name='former'),       
    url(r'^forms/', views.forms, name='forms'),
]


