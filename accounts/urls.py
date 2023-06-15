from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name = "signup"),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = "logout"),
    path('homepage/', views.homepage_view, name = "homepage"),
    path('profile/', views.profile_view, name = "profile"),
]