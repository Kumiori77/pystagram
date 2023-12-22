
from django.urls import path
from . import views

# 미디어 파일 업로드 위해 추가
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("<int:user_id>/profile/", views.ProfileView.as_view(), name="profile"),
    path("<int:user_id>/followers/", views.Followers.as_view(), name="followers"),
    path("<int:user_id>/following/", views.Following.as_view(), name="following"),

]

app_name = "users"

# 미디어 파일 업로드 위해 추가
# urlpatterns += static(
#     prefix = settings.MEDIA_URL,
#     document_root = settings.MEDIA_ROOT,
# )