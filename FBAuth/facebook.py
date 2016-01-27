
from django.conf import settings
from django.shortcuts import  redirect, HttpResponse
from django.contrib.auth.models import User
from social.exceptions import AuthCanceled, AuthAlreadyAssociated #social_auth.exceptions.StopPipeline
#from social_auth.exceptions import AuthAlreadyAssociated, AuthCanceled 
#from social_auth.middleware import SocialAuthExceptionMiddleware

#from social.pipeline.partial import partial

def check_if_exists(strategy, *args, **kwargs):
    #request = kwargs.get('request')
    if kwargs['is_new']:
        if strategy.request.GET.get('login_type') == 1:  #need to add message
            raise AuthCanceled
    else: 
        if strategy.request.GET.get('login_type') == 2: 
            raise AuthAlreadyAssociated          #need to add message
            #return redirect('login', message = 'User for this account is already exist, try to login')
            #raise AuthAlreadyAssociated
    return None

"""
def last_check(strategy, user, *args, **kwargs):
    if user.last_login != user.date_joined:
        redirect('/new_user')
    else:
   """     