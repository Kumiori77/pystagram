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

    # 해시태그 다대다 관계
    tags = models.ManyToManyField("posts.HashTag", verbose_name="해시태그 목록", blank=True)


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


class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

    def __str__(self):

        return self.name