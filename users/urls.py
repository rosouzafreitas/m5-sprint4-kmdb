from django.urls import path
from . import views



urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path("users/register/", views.UserRegisterView.as_view()),
]
