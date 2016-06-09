from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from .forms import UsersForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    return render(request, 'users/register.html')#'home/register.html')

def createUser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UsersForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = User.objects.create_user(name)
            #user.last_name = 'lastname'
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('users:register'))
    return render(request, 'users/register.html', {'error_message': "Deine Eingaben sind falsch! Bitte versuchen Sie es erneut!",})


