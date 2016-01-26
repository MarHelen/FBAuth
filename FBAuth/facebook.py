
#from django.conf import settings
from django.shortcuts import  redirect
from django.contrib.auth.models import User
from social_auth.exceptions import AuthCanceled #social_auth.exceptions.StopPipeline

#from social.pipeline.partial import partial

def check_if_exists(*args, **kwargs):
    #request = kwargs.get('request')
    if kwargs['is_new']:
        if request.session['login_type'] == 'login': #need to add message
            raise AuthCanceled
    else: 
        if request.session['login_type'] == 'signup':  #need to add message
            raise AuthCanceled
    return None
