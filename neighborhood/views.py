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
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('users-profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'users/profile.html', {"form":form})


def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'main/all_hoods.html', params)


@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def hood_details(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz_form = form.save(commit=False)
            biz_form.neighbourhood = hood
            biz_form.user = request.user.profile
            biz_form.save()
            return redirect('hood-details', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'main/hood-details.html', params)

def hood_members(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'main/members.html', {'members': members})

def create_post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'main/post.html', {'form': form})

@login_required(login_url='login')
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='login')
def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        params = {
            'search-results': results,
            'message': message
        }
        return render(request, 'search-results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, "search-results.html")