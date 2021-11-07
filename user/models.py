from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager #장고 유저모델 상속

# Create your models here.

# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError('The given username must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username, password, **extra_fields)

#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)

class UserModel(AbstractUser):

    username = models.CharField(max_length=128, unique=True, null=False)
    #password = models.CharField(max_length=256, null=False)
    nickname = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=256, null=False)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    # User 모델의 필수 field
    # is_active = models.BooleanField(default=True)    
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    #objects = BaseUserManager()

    # USERNAME_FIELD = 'username'
    class Meta:
        db_table = 'UserModel'