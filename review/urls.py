from django.urls import path, include
from  . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('review/<int:id>', views.reviewPage, name = 'reviewPage'),
  path('register/', views.userRegister, name='register'),
  path('login/', views.userLogin, name="login"),
  path('logout/', views.logoutUser, name = "logout"),
  path('search/',views.searchBooks, name = "search"),
  # path('searchResults/',views.searchResults, name="searchResults")
]