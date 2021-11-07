import product
from user.models import UserModel
from django.db import models

class ProductModel(models.Model):
    class Meta:
        ordering = ["-created_at"]
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    product_img = models.ImageField(blank=True, upload_to="uploads")
    product_name = models.CharField(max_length=128, null=False)
    product_type = models.CharField(max_length=128, null=False)
    product_lend_h = models.CharField(max_length=128, null=False)
    product_lend_d = models.CharField(max_length=128, null=False)
    product_location = models.CharField(max_length=128, null=False)
    product_detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #데이터 생성 시 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True) #데이터 갱신 시 현재 시간 저장

    def __str__(self):
        return self.product_name #함수에서 반환하는 속성을 기준으로 레코드를 확인


class CommentModel (models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


