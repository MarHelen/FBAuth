from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context import RequestContext

from django.core.urlresolvers import reverse

def login(request, message = None):
    context = RequestContext(request, {
         'request': request, 'user': request.user, 'message' : message})
    return render_to_response('login.html', context_instance=context)
    #return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')
def home(request, new_user = None):
    if new_user:
        if new_user == 1: #new one
            message = 'Wellcome to our app!'
        if new_user == 2: #loggined
            message = "Successfully logged in"
     
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user,
                              'message' : message})
    return render_to_response('home.html',
                              context_instance=context)
"""
def signup_confirm(request):
    templ = Template ('''
            <a href="{% url 'social:complete' 'facebook' %}?next={{ request.path }}">Are you sure to Sign Up with Facebook?</a>
            <a href='/'>Cancel</a>''')
    #if request.method == 'POST':
    #    reverse('social:complete')    
    
    
    return HttpResponse(templ.render(RequestContext(request)))    
"""    
    