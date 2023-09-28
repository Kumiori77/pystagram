from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# Create your views here.

class LoginForm(TemplateView):
    template_name = "users/login.html"

