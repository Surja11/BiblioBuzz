from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
# Create your views here.
def home(request):
  return render(request, 'review/home.html')


def reviewPage(request, slug):
  return render(request, 'review/requestPage.html')

def userRegister(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit = False)
      user.set_password(form.cleaned_data["password"])
      user.save()
      messages.success("Registration successful")
      return redirect('login')
    
  form = RegistrationForm()
  return render(request, 'review/register.html',{'form': form})

def userLogin(request):
  if request.method == "POST":
    pass
  form = LoginForm()
  return render(request, 'review/login.html',{'form': form})