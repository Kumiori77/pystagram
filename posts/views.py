from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

# Create your views here.
class FeedsView(TemplateView):
    template_name = "posts/feeds.html"

    def get(self, request, *args, **kwargs) :

        user = request.user

        # 로그인 안했으면 로그인 페이지로 이동
        if not user.is_authenticated:
            return redirect("users:login")
        else :
            return super().get(self, request, *args, **kwargs)
        



