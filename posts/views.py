from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from . import models
from . import forms

from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden

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

        context["comment_form"] = forms.CommentForm()

        return context
    
@require_POST
def comment_add(request):
    
    form = forms.CommentForm(data= request.POST)
    if form.is_valid() :

        comment = form.save(commit=False)

        comment.user = request.user

        comment.save()

        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")


@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = models.Comment.objects.get(id = comment_id)

        if comment.user == request.user:
            comment.delete()

            return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
        else :
            return HttpResponseForbidden("해당 댓글을 삭제할 권한이 없습니다.")
        



