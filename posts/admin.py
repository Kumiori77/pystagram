from django.contrib import admin
from django.http.request import HttpRequest
from . import models
import admin_thumbnails

from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

# Register your models here.

class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 1


class LikeUserInline(admin.TabularInline):
    model = models.Post.like_users.through
    verbose_name = "좋아요 한 유저"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = models.PostImage
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]
    inlines = [CommentInline, PostImageInline, LikeUserInline,]

    formfield_overrides = {
        ManyToManyField: {"widget" : CheckboxSelectMultiple}
    }


@admin.register(models.PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "photo"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "content"]


@admin.register(models.HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass