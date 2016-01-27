from django.core.urlresolvers import reverse

#from social_auth.exceptions import AuthAlreadyAssociated
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
#from social_auth.middleware import SocialAuthExceptionMiddleware
from social.exceptions import AuthCanceled, AuthAlreadyAssociated

"""
class ExampleSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def raise_exception(self, request, exception):
        return False

    def get_message(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return 'Somebody is already using that account!'
        return super(ExampleSocialAuthExceptionMiddleware, self)\
                        .get_message(request, exception)

    def get_redirect_uri(self, request, exception):
        if request.user.is_authenticated():
            return reverse('done')
        else:
            return reverse('error')
        
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
"""
from django.shortcuts import  redirect, HttpResponse
        
class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return redirect('login', args = ('Somebody is already using specified social account!',) ) # = 'Somebody is already using specified social account!')
        if isinstance(exception, AuthCanceled):
            return redirect('login', message = 'User is not yet assotiated with existent account, try to Sign up first')          
        else:
            raise exception
