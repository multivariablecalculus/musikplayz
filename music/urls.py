from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_song, name='upload_song'),
    path('make_request/', views.make_request, name='make_request'),
    path('requests/', views.view_requests, name='view_requests'),
    path('delete/<int:song_id>/', views.delete_song, name='delete_song'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
