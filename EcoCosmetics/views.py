from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Product,  Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, CreateOrderSerializer
from rest_framework.filters import SearchFilter

# Create your views here.


class ProductAPIView(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', "description")
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related("order_item")


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = (AllowAny,)


