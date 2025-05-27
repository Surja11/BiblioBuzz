from django.urls import path, include
from  . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('review/<int:id>', views.reviewPage, name = 'reviewPage'),
  path('register/', views.userRegister, name='register'),
  path('login/', views.userLogin, name="login"),
  path('logout/', views.logoutUser, name = "logout"),
  path('search/',views.searchBooks, name = "search"),
  path('like/<int:review_id>/',views.like_review, name = "like_review"),
  path('comment/<int:review_id>/',views.review_comment,name="review_comment"),
  path("comments/<int:review_id>/", views.get_comments,name = "get_comments"),
  path('profile/<int:profile_id>/', views.profile, name="profile"),
  path('editProfile/<int:profile_id>/', views.editProfile, name = "editProfile"),
  path("delete/<int:review_id>/", views.deleteReview, name = "delete"),
  path("allBooks/",views.allBooks, name="allBooks")
  # path('searchResults/',views.searchResults, name="searchResults")
]