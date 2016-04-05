from django.conf.urls import url

from . import views

app_name = 'mande'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^index/$', views.IndexView.as_view(), name='index'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<job_id>[0-9]+)/results/$', views.results, name='results'),
#    url(r'^(?P<job_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
