from django.contrib import admin
#from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (main,
                    RegisterView,
                    AboutMeView,
                    ProfileUpdateView,
                    asd,
                    AddImageView,
                    logout_view,
                    CustomLoginView,
                    delete_image
                    )

# ITS home urls file, starts from home/
urlpatterns = [
    path('login/', CustomLoginView.as_view() ,name='login'),
    path('logout/',logout_view , name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('about-me/', AboutMeView.as_view(), name="about-me"),
    path('update-about-me/', ProfileUpdateView.as_view(), name="update-about-me"),
    path('add-image/',AddImageView.as_view(), name = "add-image"),
    path('image/delete/<int:image_id>/', delete_image, name="delete-image"),
    path('', main, name='main'),
]
