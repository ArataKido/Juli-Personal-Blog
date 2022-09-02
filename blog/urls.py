from django.urls import path

from . import views


urlpatterns = [
	path('', views.HomePage.as_view(), name = "home"),
	path('post/id/<int:pk>',views.PostView.as_view(), name = "post_view"),
]