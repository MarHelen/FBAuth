from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context import RequestContext

from django.core.urlresolvers import reverse
import logging
logger = logging.getLogger(__name__)


def login(request, new_user=None):
    """
    This is the main view function.
    If the user is authorized, page with his/her name will be shown
    If the user isn't, the page with 2 buttons: login and signup will be shown.
    Function recieves parameter new_user, as a message or type of login.
    """
    logger.debug("From login view, new_user = %s", new_user)
    message = 'Welcome to application!'
    if new_user:
        if new_user == 1: #new one
            message = 'Wellcome to our app! Thanks for registration'
        else: 
            if new_user == 2: #loggined
                message = "Successfully logged in"
            else:
                message = new_user
    context = RequestContext(request, {
         'request': request, 'user': request.user, 'message' : message})
    return render_to_response('login.html', context_instance=context)

@login_required(login_url='/')
def logout(request):
    """
    This is a view function for simple django logout,
    it's shown, when user was assotiated on the login page.
    """
    auth_logout(request)
    return redirect('/')