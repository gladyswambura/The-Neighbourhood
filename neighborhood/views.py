from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='/accounts/login/')
def profile(request): 
    current_user = request.user
    user = current_user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('users-profile')
        
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'users/profile.html', {"form":form})

def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)


def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'main/newhood.html', {'form': form})