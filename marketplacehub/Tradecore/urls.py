from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('verify-email/<int:user_id>/', views.verify_email),
    path('login/', views.login),
    path('profile/', views.profile),
    path('delete-account/', views.delete_account),
]

