from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()  # Основное содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания поста
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления поста
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Автор поста
