# from django.shortcuts import render

from django.core import serializers
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.filters import SearchFilter
from django.http.response import HttpResponse 
from .models import CommentModel, ProductModel 
from .serializers import CommentSerializer, ProductSerializer


class SearchViewSet(viewsets.ModelViewSet): 
    permission_classes = [AllowAny]

    queryset = ProductModel.objects.all() 
    serializer_class = ProductSerializer 

    def get_queryset(self): # 내부에서 쿼리셋을 작성 
        qs = super().get_queryset() # qs = qs.filter(author_id = 1) # .filter 또는 .exclude 
        
        # 지금 만약 로그인이 되어있다면, 로그인한 유저의 글만 필터링 
        if self.request.user.is_authenticated: 
            qs = qs.filter(author=self.request.user) # 만약 로그인이 되어있지 않다면, 비어있는 쿼리셋을 리턴 
        else: 
            qs = qs.none() 
            return qs

class SearchViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny] 

    queryset = ProductModel.objects.all() 
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter] 
    search_fields = ('product_name', 'product_detail', 'product_location',)


class ProductViewSet(viewsets.ModelViewSet): #상품 등록 API
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    #모델을 생성할 때 해당 함수를 호출한 후 현재 user 정보를 전달
    def perform_create(self, serializer):
       serializer.save(author = self.request.user)


class Product_Detail_View(APIView): #등록된 상품 상세 정보 API(CRUD)
    permission_classes = [AllowAny]

    def get_object(self, pk):
        product = get_object_or_404(ProductModel, pk=pk)
        return product

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
