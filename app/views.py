from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    response=HttpResponse("<h2>Welcome to MywebSite </h2>")
    return response