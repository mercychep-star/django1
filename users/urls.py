from django.urls import path
from .views import *
from django.contrib.auth import views as authViews

app_name = "users"
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', UserloginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('update-profile/<slug:slug>/', UserProfileUpdateView.as_view(), name="update_profile"),
    path('password-change/', authViews.PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', authViews.PasswordChangeDoneView.as_view(), name="password_change_done"),

]
