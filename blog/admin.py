from django.contrib import admin

# Register your models here.

from .models import Article
# 注册之后 可以在 Django admin 的数据库中 查看
admin.site.register(Article)
