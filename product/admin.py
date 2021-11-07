from product.models import ProductModel, CommentModel
from django.contrib import admin
from .models import CommentModel, ProductModel

admin.site.register(ProductModel)
admin.site.register(CommentModel)