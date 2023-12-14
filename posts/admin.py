from django.contrib import admin
from . import models
import admin_thumbnails

# Register your models here.

class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 1

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = models.PostImage
    extra = 1



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]
    inlines = [CommentInline, PostImageInline,]


@admin.register(models.PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "photo"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "content"]

