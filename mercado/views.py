from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

def produto(request):
    return render(request, "./produto.html")

def login(request):
    return render(request, "./login.html")