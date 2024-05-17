from django.db import models


# Create your models here.
class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)

    # 在Django admin 的数据库中显示自己的title，而不是object
    def __str__(self):
        return self.title
