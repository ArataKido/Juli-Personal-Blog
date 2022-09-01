from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
	template_name = "juli/01-homepage.html"