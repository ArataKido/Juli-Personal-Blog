
from django.db import models

# Create your models here.

class Post(models.Model):
	CHOICE = (
		('TRAVEL', 'TRAVEL'),
		('FASHION', 'FASHION'),
		('LIFESTYLE', 'LIFESTYLE'),
		('DESIGN', 'DESIGN'),
		('MUSIC', 'MUSIC'),
		('VIDEO', 'VIDEO'),
		('ADVANTRUE', 'ADVANTRUE'),
		)

	title = models.CharField(max_length=125)
	description = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=20,choices=CHOICE)
	content = models.TextField()
	# image = models.ImageField()

	def __str__(self) -> str:
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'