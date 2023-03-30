from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators  import user_passes_test


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')



def profile(request):
    return render(request, 'dashboard/profile.html')

def plagerism(request):
	return render(request, 'dashboard/plagerism.html')

def content(request):
	return render(request, 'dashboard/content.html')


