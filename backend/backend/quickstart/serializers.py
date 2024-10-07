from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from quickstart.models import Product,Brand

class UserSerializer(serializers.HyperlinkedModelSerializer):
     password = serializers.CharField(
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
     class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data.get('password'))
            return super(UserSerializer, self).create(validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'