from django.urls import path, include
from  . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('review/<str:slug>', views.reviewPage, name = 'reviewPage'),
  path('register/', views.userRegister, name='register'),
  path('login/', views.userLogin, name="login"),
]