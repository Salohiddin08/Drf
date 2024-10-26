from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category-detail'),

    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/', views.ProductAPIView.as_view(), name='product-list-create'),
    
    path('orders/', views.OrderAPIView.as_view(), name='order-list-create'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order-detail'),
    
    path('users/', views.UserAPIView.as_view(), name='user-detail'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
]