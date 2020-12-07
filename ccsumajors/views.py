from django.shortcuts import render, redirect
from .models import CCSUMajors


# Create your views here.
def view_index(request):
    return render(request, 'ccsumajors/index.html')


def view_degree(request):
    return render(request, 'ccsumajors/degreetree.html')
