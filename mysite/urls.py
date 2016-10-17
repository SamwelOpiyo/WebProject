from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^book', views.home, name='book'),
    url(r'^former/', views.former, name='former'),       
    url(r'^forms/', views.forms, name='forms'),
    url(r'^time/$', views.time, name='time'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


