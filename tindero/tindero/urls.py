from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('registration.urls')),
    url(r'^', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)