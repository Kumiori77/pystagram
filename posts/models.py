from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )

    content = models.TextField("내용")

    created = models.DateTimeField("등록일", auto_now_add=True)


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )

    photo = models.ImageField("사진", upload_to="post")


class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )

    content = models.TextField("내용")
    created = models.DateTimeField("작성일", auto_now_add=True)
