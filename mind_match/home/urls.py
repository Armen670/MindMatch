from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (main,
                    RegisterView,
                    AboutMeView,
                    ProfileUpdateView,
                    )

# ITS home urls file, starts from home/
urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'home/login.html',
                                    redirect_authenticated_user = True),
                                    name='login'),
    path('register/', RegisterView.as_view(), name="register"),
    path('about-me/', AboutMeView.as_view(), name="about-me"),
    path('update-about-me/<int:pk>/', ProfileUpdateView.as_view(), name="update-about-me"),
    path('', main, name='main'),
]
