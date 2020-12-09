from django.shortcuts import render, redirect
from .models import CCSUMajors
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Besting
from django.contrib.auth import authenticate
from .forms import SignUpForm


# Create your views here.
def view_index(request):
    return render(request, 'ccsumajors/index.html')


def view_degree(request):
    return render(request, 'ccsumajors/degreetree.html')


def view_login(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(data=request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect('index')
    else:
        loginForm = AuthenticationForm()
    context = {'loginForm': loginForm}
    return render(request, 'ccsumajors/login.html', context)


def view_register(request):
    if request.method == 'POST':
        registerForm = SignUpForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('index')
        else:
            messages.info(request, 'Error')
            return redirect('register')
    else:
        registerForm = SignUpForm()
    context = {'registerForm': registerForm}
    return render(request, 'ccsumajors/register.html', context)


"""
def view_register(request):
    if request.method == 'POST':
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('index')
    else:
        registerForm = UserCreationForm()
    context = {'registerForm': registerForm}
    return render(request, 'ccsumajors/register.html', context)
"""


def view_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def view_project(request):
    return render(request, 'ccsumajors/projects.html')
