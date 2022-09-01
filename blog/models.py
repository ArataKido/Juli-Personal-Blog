
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
	image = models.ImageField(upload_to='media/', null=True)

	def __str__(self) -> str:
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'


class Coment(models.Model):
	"""This class saves data in database
	Args:
		models : is used to reffer to class models
	Returns:
		_str_: returns data in str format
	"""
	name = models.CharField(max_length=32)
	email = models.EmailField('Email', max_length=50)
	message = models.CharField('Message', max_length=120)
	subject = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.name} {self.subject} {self.email} {self.message}'

	class Meta:
		# changes name of this model in db
		verbose_name = "Coment"
		verbose_name_plural = "Coments"