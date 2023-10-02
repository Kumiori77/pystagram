from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# Create your views here.
class FeedsView(TemplateView):
    template_name = "posts/feeds.html"


