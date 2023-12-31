# from typing import Any
# from django import http
from django.http import HttpResponseRedirect
from typing import Any
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from . import forms
from . import models

# 로그인 처리를 위해 추가
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class LoginView(FormView):
    template_name = "users/login.html"

    form_class = forms.LoginForm

    success_url = reverse_lazy("posts:feeds")

    
    def get(self, request, *args, **kwargs):

        user = request.user

        # 이미 로그인 했다면 피드 페이지로 이동    
        if user.is_authenticated:
            return redirect("posts:feeds")
        else :
            return super().get(self, request, *args, **kwargs)
        
    # 폼이 전달될 때 호출
    def form_valid(self, form):

        # 폼에 전달된 데이터가 유효하면
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # 해당하는 유저가 있는지 확인
            user = authenticate(username=username, password=password)

            # 해당하는 유저가 있다면
            if user:
                login(user=user, request=self.request)
                return redirect("posts:feeds")
            else :
                form.add_error(None, "해당하는 사용자가 없습니다.")

        # return super().form_valid(form)

        # return redirect("users:login")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(View):

    def get(self, request, *args, **kwargs):

        # 로그아웃 처리
        logout(request=request)

        # 로그인 화면으로 리다이렉트s
        return redirect("users:login")
    
    
class SignupView(FormView):
    template_name="users/signup.html"

    form_class = forms.SignupForm

    success_url = reverse_lazy("posts:feeds")

    # 폼이 전달되면 호출
    def form_valid(self, form) :
        
        # 폼이 유효한지 확인
        if form.is_valid():
            # 회원가입
            user = form.save()

            # 로그인
            login(user=user, request=self.request)

            return super().form_valid(form)
        
        else :
            return self.render_to_response(self.get_context_data(form=form))
        
       
class ProfileView(TemplateView):

    template_name = "users/profile.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        user_id = kwargs["user_id"]
        user = get_object_or_404(models.User, id=user_id)

        context["user"] = user
        
        return context


class Followers(TemplateView):
    template_name = "users/followers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = kwargs["user_id"]

        user = get_object_or_404(models.User, id=user_id)
        relationships = user.follower_relationships.all()

        context["user"] = user
        context["relationships"] = relationships

        return context
    
class Following(TemplateView):
    template_name = "users/following.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = kwargs["user_id"]

        user = get_object_or_404(models.User, id=user_id)
        relationships = user.following_relationships.all()

        context["user"] = user
        context["relationships"] = relationships

        return context


def follow(request, user_id):
    user = request.user
    target_user = models.User.objects.get(id=user_id)

    # 이미 팔로우 하는 경우
    if target_user in user.following.all():
        user.following.remove(target_user)
    
    # 새로 팔로우 하는 경우
    else :
        user.following.add(target_user)

    url = request.GET.get("next") or reverse_lazy("users:profile", args=[user.id])

    return HttpResponseRedirect(url)

