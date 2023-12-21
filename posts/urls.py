
from django.urls import path
from . import views

# 미디어 파일 업로드 위해 추가
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("feeds/", views.FeedsView.as_view(), name="feeds"),
    path("comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>", views.comment_delete, name="comment_delete"),
    path("post_add/", views.PostAdd.as_view(), name="post_add"),
    path("tags/<str:tag_name>/", views.Tags.as_view(), name="tags"),
    path("<int:post_id>/", views.PostDetail.as_view(), name="post_detail"),
    path("<int:post_id>/like/", views.psot_like, name="post_like"),
]

app_name = "posts"

# 미디어 파일 업로드 위해 추가
# urlpatterns += static(
#     prefix = settings.MEDIA_URL,
#     document_root = settings.MEDIA_ROOT,
# )