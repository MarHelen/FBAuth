from django.conf.urls.static import static
from django.conf import settings

from FBAuth.views import *

from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin

from FBLogin.config import *

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'FBAuth.views.login'),
    url(r'^home/$', 'FBAuth.views.home'),
    url(r'^logout/$', 'FBAuth.views.logout'),
    url(r'^new_user/$', 'FBAuth.views.login', {'new_user' : 1}),
    url(r'^succeeded/$', 'FBAuth.views.login', {'new_user' : 2}),
    #url(r'^signup_confirm/$', 'FBAuth.views.signup_confirm'),
    url(r'^login_error/$', 'FBAuth.views.login', {'message' : 'Error while attempt to login'}),
)