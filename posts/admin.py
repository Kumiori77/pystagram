from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]

@admin.register(models.PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "photo"]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "content"]

