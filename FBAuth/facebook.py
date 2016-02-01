
from django.conf import settings
from django.shortcuts import  redirect, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
<<<<<<< HEAD
from social.exceptions import AuthCanceled, AuthAlreadyAssociated 
from . import views
=======
from social.exceptions import AuthCanceled, AuthAlreadyAssociated #social_auth.exceptions.StopPipeline
from . import views
#from social_auth.exceptions import AuthAlreadyAssociated, AuthCanceled 
#from social_auth.middleware import SocialAuthExceptionMiddleware
>>>>>>> be3fa6a7a31323f468e726ce99057468b8f27dda

import logging
logger = logging.getLogger(__name__)

<<<<<<< HEAD
=======
# import the logging library
#import logging


#from social.pipeline.partial import partial

#@partial
>>>>>>> be3fa6a7a31323f468e726ce99057468b8f27dda
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
<<<<<<< HEAD
    logger.debug("is_new parameter is %s", kwargs['is_new'])
    logger.debug("login_type is %s", login_type)
    if kwargs['is_new']:
        if login_type == 1: 
            raise AuthCanceled
    else:
        if login_type == 2: 
            raise AuthAlreadyAssociated
    return None
=======
    #login_type = strategy.session_get('login_type')
    #login_type = request['login_type']
    #login_type = strategy.request['login_type']
    logger.debug("is_new parameter is %s", kwargs['is_new'])
    logger.debug("login_type is %s", login_type)
    if kwargs['is_new']:
        if login_type == 1:  #need to add message
            return redirect('/', message ='Specified social account is not yet associated with any existent user, try to Sign up first')
            #raise AuthCanceled
    else:
        #if login_type == 2: 
            #raise AuthAlreadyAssociated          #need to add message
            new_user = 1
            return redirect('/new_user/1/')
            #return redirect('/new_user/', {'new_user' : new_user} )
            #return login(new_user=1)
            #return redirect(reverse('new_user'))
            #reverse('FBAuth.views.login', kwargs={'new_user' : new_user} ) #, new_user=new_user) #, args =(new_user,))
            #reverse(redirect_uri, args=(backend,))
            #raise AuthAlreadyAssociated
    return None
        
>>>>>>> be3fa6a7a31323f468e726ce99057468b8f27dda
