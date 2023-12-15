from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from . import models

# Create your views here.
class FeedsView(TemplateView):
    template_name = "posts/feeds.html"
        
    def get_context_data(self, **kwargs) :

        user = self.request.user
        # 로그인 안했으면 로그인 페이지로 이동
        if not user.is_authenticated:
            return redirect("users:login")

        context = super().get_context_data(**kwargs)

        context["posts"] = models.Post.objects.all()

        return context
        



