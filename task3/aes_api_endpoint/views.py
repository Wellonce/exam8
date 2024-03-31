from rest_framework import generics
from task3.aes_api_endpoint.serializers import ProductSerializer
from task3.models import Product


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


__all__ = ['ProductListCreate', ]
