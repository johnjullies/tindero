from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^register/', views.register, name='register'),
)