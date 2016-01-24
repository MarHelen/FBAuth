
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context import RequestContext
#from django.contrib.auth.views import logout


def login(request):
    context = RequestContext(request, {
         'request': request, 'user': request.user})
    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #user.save()
    return render_to_response('login.html', context_instance=context)
    #return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/')
def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)