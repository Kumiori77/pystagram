from django import forms
from django.core.exceptions import ValidationError
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder":"사용자명 (3자리 이상)"},
        ),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder":"비밀번호 (4자리 이상)"}
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    # 유저네임 유효성 검사
    def clean_username(self):
        username = self.cleaned_data["username"]
        if models.User.objects.filter(username=username).exists():
            raise ValidationError("{}는 이미 사용중인 유저네임 입니다.".format(username))
        return username
    
    # 비밀번호 확인 유효성 검사
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
         # 비밀번호 확인
        if password1 != password2:
            self.add_error("password2", "비밀번호가 일치하지 않습니다...")

    # 회원가입 메소드
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]
        
        user = models.User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            short_description=short_description,
        )
        return user

