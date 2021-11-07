# from django.shortcuts import render, redirect
# from rest_framework import viewsets
# from django.http import HttpResponse, JsonResponse

from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from django.http.response import HttpResponse 
from .models import UserModel 
from .serializers import UserSerializer, LoginSerializer

# JWT 사용을 위해 필요
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#from rest_framework_jwt.serializers import VerifyJSONWebTokenSerialize

@api_view(['GET'])
@permission_classes ([IsAuthenticated])
def getuser(request):
    if request.method == 'GET':
        # users = request.user.is_authenticated
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes ([AllowAny])
def createuser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


#         if UserModel.objects.filter(username=serializer.validated_data['username']).first() is None:
#             serializer.save()
#             return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
#         return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
@permission_classes ([AllowAny])
def login(request):
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)

            if not serializer.is_valid(raise_exception=True):
                return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
            if serializer.validated_data['username'] == "None":
                return Response({'message': 'fail'}, status=status.HTTP_200_OK)

            response = {
                'success': 'True',
                'username': serializer.data['username'],
                'token': serializer.data['token']
            }
            return Response(response, status=status.HTTP_200_OK)

# 해당 html을 띄워주는 함수
# def sign_up_view(request):
#     if request.method == 'GET':
#         #return HttpResponse("@@")
#         object = UserModel.objects.all()
#         post_list = serializers.serialize('json', object)
#         return HttpResponse(post_list, content_type="text/json-comment-filtered")
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=200)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
            
            # username = request.POST.get('username', None)
            # password = request.POST.get('password', None)
            # nickname = request.POST.get('nickname', None)
            # phone = request.POST.get('phone', None)
            # #post 요청에 담겨진 데이터를 받아옴

            # new_user = UserModel()
            # new_user.username = username
            # new_user.password = password
            # new_user.nickname = nickname
            # new_user.phone = phone
            # new_user.save()
          #return HttpResponse('회원가입 완료!') #회원가입 완료 시 로그인 페이지 실행
