
from django.conf import settings
from django.shortcuts import  redirect, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from social.exceptions import AuthCanceled, AuthAlreadyAssociated 
from . import views

import logging
logger = logging.getLogger(__name__)

def check_if_exists(strategy,  request, *args, **kwargs):
    """
    This is custom pipeline function, which is designed to check
    if assotiating user is already exist and what type of ligin are specifying.
    If user do login-ing, but it's not yet associated with an existent account,
    exception AuthCanceled raises;
    If user is assoiciated, but sign-ing doing, exception AuthAlreadyAssociated
    raises. These exeptions catches in middleware.py
    """
    login_type = strategy.request.GET.get('login_type')
    logger.debug("is_new parameter is %s", kwargs['is_new'])
    logger.debug("login_type is %s", login_type)
    if kwargs['is_new']:
        if login_type == 1: 
            raise AuthCanceled
    else:
        if login_type == 2: 
            raise AuthAlreadyAssociated
    return None