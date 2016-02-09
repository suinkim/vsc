from django.conf.urls import url

from . import views

app_name = 'mande'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.detail(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<job_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
