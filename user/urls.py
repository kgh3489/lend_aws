from django.urls import path
from . import views

urlpatterns = [
    path('user/signup/', views.createuser, name='user-signup'),
    path('user/info/', views.getuser, name='user-info'),
    path('user/login/', views.login, name='user-login'),
    #도메인 접속 -> views의 해당 뷰의 함수 실행
]