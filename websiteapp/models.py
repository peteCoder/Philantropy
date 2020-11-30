from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.



class AboutPage(models.Model):
	overall_title_in_red_letters = models.CharField(max_length=1000, blank=True, null=True)
	first_content_title = models.CharField(max_length=1000, blank=True, null=True)
	first_content = RichTextField(blank=True, null=True)
	image_of_first_content= models.ImageField(upload_to="Blogapp/images/", blank=True, null=True)
	second_content_title = models.CharField(max_length=1000, blank=True, null=True)
	second_content = RichTextField(blank=True, null=True)
	image_of_second_content = models.ImageField(upload_to="Blogapp/images/", blank=True, null=True)

	class Meta:
		verbose_name_plural = "About"

	def __str__(self):
		return "Post " + str(self.id)


class RecentEvents(models.Model):

	name_of_event = models.CharField(max_length=1000, blank=True, null=True)
	about_event = RichTextField("Write about Event", blank=True, null=True)
	image_of_event = models.ImageField(upload_to="Blogapp/images/", blank=True, null=True)

	class Meta:
		verbose_name_plural = "Recent Events"

	def __str__(self):
		return "Event " + str(self.id)


class Help(models.Model):
	image = models.ImageField(upload_to="Blogapp/images", blank=True, null=True)
	name = models.CharField(max_length=400, blank=True, null=True)
	child_story = RichTextField("child's story", blank=True, null=True)


	def __str__(self):
		return self.name.title() + "'s " + "Story"

	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Help The Little Children"



class Team(models.Model):
	team_image = models.ImageField(upload_to="images/gallery/",null=True, blank=True)
	name = models.CharField(max_length=255, blank=True, null=True)
	position = models.CharField(max_length=255, blank=True, null=True)
	facebook_url = models.CharField(max_length=255, blank=True, null=True)
	twitter_url = models.CharField(max_length=255, blank=True, null=True)
	instagram_url = models.CharField(max_length=255, blank=True, null=True)
	pinterest_url = models.CharField(max_length=255, blank=True, null=True)
	linkedin_url = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Our Team"

	def __str__(self):
		return self.name

class Testimonial(models.Model):
	testifier_image = models.ImageField(upload_to='images/Testimony')
	testifier_name = models.CharField(max_length=100)
	remark = models.CharField(max_length=100, default="")
	testimonies = models.TextField(max_length=1000)

	def __str__(self):
		return self.testifier_name

	class Meta:
		verbose_name_plural = "Testimonial"


class Gallery(models.Model):

	image_one = models.ImageField("image", upload_to="images/gallery/",null=True, blank=True,)
	image_one_title = models.CharField("image title", max_length=100,null=True, blank=True,)
	image_one_text = models.CharField("image description", max_length=100,null=True, blank=True,)


	def __str__(self):
		return self.image_one_title

	class Meta:
		verbose_name_plural = "Our Activities Gallery"


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=200)
	message = models.TextField(blank=False, null=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Contact Us"


class ShortDiscriptionInAboutPage(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	first_letter_of_name_in_capital_letter = models.CharField("first letter of 'name' in capital letter", max_length=1, blank=True, null=True)
	flaticon = models.CharField("flaticon class", max_length=100, blank=True, null=True)
	short_description = models.TextField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = "A Short Description on Vision, Mission, History, Goal, etc."
		ordering = ["pk"]
