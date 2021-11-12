from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import *
from django.forms import ModelForm
from django.views import generic
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate

#views

def index(request):
    activities = Activity.objects.all()
    return render(request, 'index.html', {'activities' :activities})





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('avatar')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# signup
class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('avatar')
    template_name = 'registration/signup.html'


# map
@login_required
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})


# activity page
def activity(request):
    return render(request, 'activity-page.html')


# about page
def about(request):
    return render(request, 'about.html')

# history page
def history(request):
    activities = Activity.objects.all()
    return render(request, 'history.html', {'activities' :activities})

def favourites(request):
    activities = Activity.objects.all()
    return render(request, 'favourites.html', {'activities' :activities})

class ActivityListView(generic.ListView):
    model = Activity


class ActivityDetailView(generic.DetailView):
    model = Activity


@login_required
def create_activity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateActivity(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/activities/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateActivity()

    return render(request, 'create-activity-page.html', {'form': form})


# def longlat(request):
#     activity_list = Activity.objects.all()
#     context = {
#         'activity_list': activity_list
#     }
#     return render(request, 'longlat.html', context)


def avatar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileFormAvatar(request.POST, instance=request.user)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/postcode')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileFormAvatar()
    return render(request, 'registration/avatar.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def postcode(request):
    return render(request, 'registration/enter-your-post-code.html')