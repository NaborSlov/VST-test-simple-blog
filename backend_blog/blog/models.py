from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class Blog(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, related_name="blogs", null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Comment(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, related_name="comments", null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Блог:{self.blog.id} Комментарий:{self.id}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
