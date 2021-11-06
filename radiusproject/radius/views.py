from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import *
from django.forms import ModelForm
from django.views import generic
from .models import Activity

#views

def index(request):
    activities = Activity.objects.all()
    return render(request, 'index.html', {'activities' :activities})


def signin(request):
    return render(request, 'sign-in-page.html', {'title': 'Sign in'})


# login
def login(request):
    return render(request, 'login.html')


# signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #process signup
            return HttpResponseRedirect('avatar.html')
    else:
        context = {
            'form': SignUpForm,
        }
        return render(request, 'registration/signup.html', context)


# map
@login_required
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})


# create activity
def create_activity(request):
    return render(request, 'create-activity-page.html')


# activity page
def activity(request):
    return render(request, 'activity-page.html')


# about page
def about(request):
    return render(request, 'about.html')

# history page
def history(request):
    return render(request, 'history.html')

# history page
def favourites(request):
    return render(request, 'favourites.html')

class ActivityListView(generic.ListView):
    model = Activity


class ActivityDetailView(generic.DetailView):
    model = Activity


class ActivityModelForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'