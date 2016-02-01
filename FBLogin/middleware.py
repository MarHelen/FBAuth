from django.core.urlresolvers import reverse
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social.exceptions import AuthCanceled, AuthAlreadyAssociated
from django.shortcuts import  redirect, HttpResponse
        
class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    """
    Class designed to catch exception from facebook.py raised,
    if authorization has to be cancelet by some reason.
    I case of catching, user redirects back to login page with appropriate error message
    """
    def process_exception(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return redirect('login', new_user = 'Somebody is already using specified social account!',)
        if isinstance(exception, AuthCanceled):
            return redirect('login', new_user = 'User is not yet assotiated with existent account, try to Sign up first')          
        else:
            raise exception
