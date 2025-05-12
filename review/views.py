from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
  return render(request, 'review/home.html')

@login_required
def reviewPage(request, slug):
  return render(request, 'review/requestPage.html')

def userRegister(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    print("form is delivered")
    if form.is_valid():
      print("form is checked")
      user = form.save(commit = False)
      user.set_password(form.cleaned_data["password"])
      user.save()
      messages.success(request,"Registration successful")
      return redirect('login')
    
        
  form = RegistrationForm()
  return render(request, 'review/register.html',{'form': form})

def userLogin(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == "POST":
    print("post activated")
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not email or not password:
      messages.error(request, "Both fields are required")
      return redirect('login')
    
    try:
      user = User.objects.get(email = email)
      print("no email")
    except User.DoesNotExist:
      messages.error(request, "Invalid email or password.")
      print("user does not exist") 
    
    user = authenticate(request, email = email, password = password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      print(messages.error)
      messages.error(request, "Invalid email or password")
  return render(request, 'review/login.html')

def logoutUser(request):
  logout(request)
  return render(request, 'review/register.html')

