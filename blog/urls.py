from django.urls import path, include

import blog.views

# 应用级路由
urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content)
]
