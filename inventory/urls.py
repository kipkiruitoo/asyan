from django.urls import path, include
from . import views

app_name = 'inventory'

urlpatterns = [
    ######################################################################################################
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/new/', views.ProductsCreateView.as_view(), name='products_new'),
    path('products/detail/<int:pk>/', views.ProductsDetailView.as_view(), name='products_detail'),
    path('products/update/<int:pk>/', views.ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', views.ProductsDeleteView.as_view(), name='products_delete'),
    ##############################################################################################################3
    
      ######################################################################################################
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/new/', views.ProductsCreateView.as_view(), name='products_new'),
    path('products/detail/<int:pk>/', views.ProductsDetailView.as_view(), name='products_detail'),
    path('products/update/<int:pk>/', views.ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', views.ProductsDeleteView.as_view(), name='products_delete'),
    ##############################################################################################################3
      ######################################################################################################
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_new'),
    path('category/detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
    ##############################################################################################################3
      ######################################################################################################
    path('pallet/', views.PalletListView.as_view(), name='pallet_list'),
    path('pallet/new/', views.PalletCreateView.as_view(), name='pallet_new'),
    path('pallet/detail/<int:pk>/', views.PalletDetailView.as_view(), name='pallet_detail'),
    path('pallet/update/<int:pk>/', views.PalletUpdateView.as_view(), name='pallet_update'),
    path('pallet/delete/<int:pk>/', views.PalletDeleteView.as_view(), name='pallet_delete'),
    ##############################################################################################################3
]