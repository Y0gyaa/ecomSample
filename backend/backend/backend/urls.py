"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import quickstart.views as v 


router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new-user/',v.UserCreateView.as_view(),name='User-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('products/', v.ProductListCreateView.as_view(), name='Product-list-create'),
    path('products/<int:pk>/', v.ProductDetailView.as_view(), name='Product-detail'),
    path('products/all/', v.AllProductsListView.as_view(), name='all-Products-list'),  
    path('products/delete/<int:pk>/', v.ProductDeleteView.as_view(), name='Product-delete'), 
    path('products/update/<int:pk>/', v.ProductUpdateView.as_view(), name='Product-update'), 
    path('brands/', v.BrandListCreateView.as_view(), name='Brand-list-create'),
    path('brands/<int:pk>/', v.BrandDetailView.as_view(), name='Brand-detail'),
    path('brands/all/', v.AllBrandsListView.as_view(), name='all-Brands-list'),  
    path('brands/delete/<int:pk>/', v.BrandDeleteView.as_view(), name='Brand-delete'), 
    path('brands/update/<int:pk>/', v.BrandUpdateView.as_view(), name='Brand-update'), 
    
]
   
