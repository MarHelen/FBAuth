from django.conf.urls.static import static
from django.conf import settings

from . import views

from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'FBAuth.views.login'),
    url(r'^home/$', 'FBAuth.views.home'),
    url(r'^logout/$', 'FBAuth.views.logout'),
)