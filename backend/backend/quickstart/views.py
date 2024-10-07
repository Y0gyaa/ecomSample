from rest_framework import generics,permissions, viewsets, filters
from quickstart.models import Product,Brand
from quickstart.serializers import ProductSerializer,BrandSerializer,UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=email']

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class AllProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    partial = True
    
    
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Product"))
    

class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    
class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class AllBrandsListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class BrandUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    partial = True
    
    
class BrandDeleteView(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Brand"))