from typing import Any
from django import http
from django.views.generic import TemplateView
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        user = request.user

        # 로그인 여부에 따라 로그인 페이지나 피드 페이지로 이동
        if user.is_authenticated:
            return redirect("posts:feeds")
        elif not user.is_authenticated:
            return redirect("users:login")

    