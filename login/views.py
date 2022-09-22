from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import LoginForm
import hashlib
from . import models

# Create your views here.

def loginpage(request):

    if request.method == 'POST':
        if not LoginForm.is_valid:
            return render(request, 'login/index.html', {
                'login_failed_previous': True,
                'form': LoginForm(),
            })
        logincheck = models.User.logincheck(request)
        if logincheck :
            return HttpResponseRedirect(reverse('login:success'))
        else :
            return render(request, 'login/index.html', {
                'login_failed_previous': True,
                'form': LoginForm(),
            })

    return render(request, 'login/index.html', {
        'login_failed_previous': False,
        'form': LoginForm(),
    })
    

def successpage(request):
    return render(request, 'login/login_success.html')


def loginfailed(request):
    return HttpResponse(request, '')