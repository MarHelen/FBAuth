from django.conf.urls.static import static
from django.conf import settings

from . import views

from django.conf.urls import include, url
from django.conf.urls import patterns
from django.contrib import admin

#from FBLogin.config import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^.*', login, name = 'login'),
    url(r'^logout/.*', logout, name = 'FBAuth.views.logout'),
    url(r'^/new_user/(?P<new_user>)/$', login, name = 'new_user' ),
    url(r'^succeeded/.*', login, {'new_user':2}, name = 'succeeded' ),
    #url(r'^signup_confirm/$', 'FBAuth.views.signup_confirm'),
    url(r'^login_error/.*', login, {'new_user' : 'Error while attempt to login'}, name = 'login_error'),
]