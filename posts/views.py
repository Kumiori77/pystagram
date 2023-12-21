from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from . import models
from . import forms

from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy

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

        
        url = request.GET.get("next") or reverse_lazy("posts:feeds") + f"#post-{comment.post.id}"

        return HttpResponseRedirect(url)


@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = models.Comment.objects.get(id = comment_id)

        if comment.user == request.user:
            comment.delete()

            url = reverse_lazy("posts:feeds") + f"#post-{comment.post.id}"
            return HttpResponseRedirect(url)
        else :
            return HttpResponseForbidden("해당 댓글을 삭제할 권한이 없습니다.")
        

class PostAdd(FormView):
    template_name = "posts/post_add.html"

    form_class = forms.PostForm


    def form_valid(self, form):

        post = form.save(commit=False)
        post.user = self.request.user
        post.save()

        for image_file in self.request.FILES.getlist("images"):
            models.PostImage.objects.create(
                post = post,
                photo = image_file,
            )

        # 해시태그 추가
        tag_str = self.request.POST.get("tags")
        if tag_str:
            # 문자열에서 태그를 추출해서 리스트로 저장
            tag_names = [tag_name.strip() for tag_name in tag_str.split(",") ]
            for tag_name in tag_names:
                tag, _ = models.HashTag.objects.get_or_create(name=tag_name)

                post.tags.add(tag)

        url = reverse_lazy("posts:feeds") + f"#post-{post.id}"
        return HttpResponseRedirect(url)
    
        
class Tags(TemplateView):

    template_name = "posts/tags.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        tag_name = kwargs["tag_name"]

        try:
            tag = models.HashTag.objects.get(name=tag_name)

        except models.HashTag.DoesNotExist:
            posts = models.Post.objects.none()
        
        else :
            posts = models.Post.objects.filter(tags=tag)
        
        context["posts"] = posts
        context["tag_name"] = tag_name
        return context
    

class PostDetail(TemplateView):

    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        postId = kwargs["post_id"]
        post = models.Post.objects.get(id = postId)
        context["post"] = post

        context["comment_form"] = forms.CommentForm()

        return context


# 좋아요 처리 메소드 
def psot_like(request, post_id):
    post = models.Post.objects.get(id=post_id)
    user = request.user

    # 좋아요가 눌려있다면
    if user.like_posts.filter(id=post_id).exists():
        user.like_posts.remove(post)
    # 좋아요가 안눌려있다면
    else : 
        user.like_posts.add(post)

    # 이동할 url
    url = request.GET.get("next") or reverse_lazy("posts:feeds") + f"#post-{post.id}"

    return HttpResponseRedirect(url)

