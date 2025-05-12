from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'review/home.html')


def reviewPage(request, slug):
  return render(request, 'review/requestPage.html')

def userRegister(request):
  return render(request, 'review/register.html')

def userLogin(request):
  return render(request, 'review/login.html')