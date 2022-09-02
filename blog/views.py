from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class HomePage(ListView):
	template_name = "juli/01-homepage.html"

	def get(self, request):
		posts = Post.objects.order_by('-date_created')[0:2]

		context = {
			'posts': posts
		}
		return render(request, self.template_name, context)

class PostView(DetailView):
	template_name = "juli/02-Single-post.html"
	
	def get(self, request, pk):
		post = Post.objects.get(pk=pk)
		return render(request, self.template_name, {"post":post} )