from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import  RichTextField
import datetime
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = "Category"

class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="Blogapp/images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title_tag = models.CharField(max_length=233)
	body = RichTextField(blank=True, null=True)
	comments = GenericRelation(Comment)
	title_intro = models.TextField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	quote = RichTextField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
	snippet = models.CharField(max_length=255, default='Read More')
	video_file = models.FileField(blank=True, null=True, upload_to="Blogapp/video/")

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + " | " + str(self.author.first_name)

	@property
	def day(self):
		date = self.date_created
		day = date.strftime("%d")
		return day

	@property
	def month(self):
		date = self.date_created
		month = date.strftime("%b").upper()
		return month

	def get_absolute_url(self):
		return reverse('home')
	

	class Meta:
		verbose_name_plural = "Blog Posts"