
from django.urls import path
from . import views

# 미디어 파일 업로드 위해 추가
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.LoginForm.as_view(), name="login"),
]

app_name = "users"

# 미디어 파일 업로드 위해 추가
# urlpatterns += static(
#     prefix = settings.MEDIA_URL,
#     document_root = settings.MEDIA_ROOT,
# )