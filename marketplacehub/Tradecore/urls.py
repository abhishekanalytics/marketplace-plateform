from django.urls import path
from . import views
from .views import product_list, product_detail, product_nearby


urlpatterns = [
    path('register/', views.register),
    path('verify-email/<int:user_id>/', views.verify_email),
    path('login/', views.login),
    path('profile/', views.profile),
    path('delete-account/', views.delete_account),
     path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('products/nearby/', product_nearby, name='product-nearby'),

]

# from django.urls import path
# from .views import product_list, product_detail, product_nearby

# urlpatterns = [
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
#     path('products/nearby/', product_nearby, name='product-nearby'),
# ]
