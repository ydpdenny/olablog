from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.contrib.auth import (login as auth_login,  authenticate)
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def globalbuster(request):
    return render(request, 'blog/globalbuster.html')


@login_required
def globalbusteractive(request):
    return render(request, 'blog/globalbusteractive.html')

def login(request):
    _message = 'Please log in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('globalbusteractive'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'blog/login.html', context)
