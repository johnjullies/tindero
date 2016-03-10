from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
	'',
	url(r'^$', views.index, name='index'),
	url(r'^nice/(?P<user_id>\d+)$', views.nice, name='nice'),
	url(r'^nope/(?P<user_id>\d+)$', views.nope, name='nope'),
	url(r'^profile/$', views.profile, name='profile'),
)