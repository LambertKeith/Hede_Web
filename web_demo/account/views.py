from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def test_view(request):
    return HttpResponse("hello")
    