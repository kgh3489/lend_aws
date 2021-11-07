from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from .models import UserModel

# JWT 사용을 위한 설정
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username','password','nickname','phone') # 필드 설정
    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=256, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password", None)
        # 사용자 아이디와 비밀번호로 로그인 구현
        user = authenticate(username=username, password=password)

        if user is None:
            return {
                'username': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user) # payload 생성
            jwt_token = JWT_ENCODE_HANDLER(payload) # jwt token 생성
            update_last_login(None, user)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'username':user.username,
            'token': jwt_token
        }