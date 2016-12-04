from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/([a-zA-Z]+)/$', views.category, name='index'),
]