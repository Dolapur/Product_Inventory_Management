from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_display, name="product_display"),
    path('products/create/', views.product_creation, name="product_creation"),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete')
]
