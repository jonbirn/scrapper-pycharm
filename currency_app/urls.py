__author__ = 'jonbirn'


from django.conf.urls import url
from currency_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]
