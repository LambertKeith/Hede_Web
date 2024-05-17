from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def show_welcome(request):
    return render(request, "welcome.html")