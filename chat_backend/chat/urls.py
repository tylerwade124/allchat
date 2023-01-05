from django.urls import path
from . import views
from .views import UserDelete

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('chat/', views.lobby, name='lobby'),
    path('password/', views.change_password, name='change_password'),
    path('<int:pk>/delete', UserDelete.as_view(), name='user_confirm_delete'),
]