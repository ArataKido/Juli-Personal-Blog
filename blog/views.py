from django.views.generic import ListView
from .models import Post
# Create your views here.


class HomePage(ListView):
	template_name = "juli/01-homepage.html"
	model = Post
	context_object_name = 'posts'