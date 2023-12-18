from django import forms
from . import models

class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = [
            "post",
            "content",
            ]
        widgets = {
            "content" : forms.Textarea(
                attrs={
                    "placeholder": "댓글 입력.."
                }
            )
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post

        fields = ["content"]