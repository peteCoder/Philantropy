from django.test import TestCase
from websiteapp.models import AboutPage, RecentEvents, Help, Team, Testimonial, Gallery, Contact, ShortDiscriptionInAboutPage

# Create your tests here.
class TestAboutPage(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.obj_id = AboutPage.objects.create(overall_title_in_red_letters="overall title in red letters").pk


	def test_overall_title_in_red_letters(self):
		about = AboutPage.objects.get(id=self.obj_id)
		length = about._meta.get_field("overall_title_in_red_letters").max_length
		blank = about._meta.get_field("overall_title_in_red_letters").blank
		null = about._meta.get_field("overall_title_in_red_letters").null
		verbose = about._meta.verbose_name_plural

		self.assertTrue(isinstance(about, AboutPage))
		self.assertEquals(about.__str__(), "Post {}".format(str(about.id)))
		self.assertEquals(length, 1000)
		self.assertEquals(verbose, "About")
		self.assertTrue(blank)
		self.assertTrue(null)

	def test_first_content_title(self):
		about = AboutPage.objects.get(id=self.obj_id)
		length = about._meta.get_field("first_content_title").max_length
		blank = about._meta.get_field("first_content_title").blank
		null = about._meta.get_field("first_content_title").null

		self.assertTrue(isinstance(about, AboutPage))
		self.assertEquals(about.__str__(), "Post {}".format(str(about.id)))
		self.assertEquals(length, 1000)
		self.assertTrue(blank)
		self.assertTrue(null)

	def test_first_content(self):
		about = AboutPage.objects.get(id=self.obj_id)
		blank = about._meta.get_field("first_content").blank
		null = about._meta.get_field("first_content").null

		self.assertTrue(blank)
		self.assertTrue(null)

	def test_image_of_first_content(self):
		about = AboutPage.objects.get(id=self.obj_id)
		blank = about._meta.get_field("image_of_first_content").blank
		null = about._meta.get_field("image_of_first_content").null
		upload = about._meta.get_field("image_of_first_content").upload_to
		image_file = "Blogapp/images/"

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(upload, image_file)

	def test_second_content_title(self):
		about = AboutPage.objects.get(id=self.obj_id)
		length = about._meta.get_field("second_content_title").max_length
		blank = about._meta.get_field("second_content_title").blank
		null = about._meta.get_field("second_content_title").null

		self.assertTrue(isinstance(about, AboutPage))
		self.assertEquals(about.__str__(), "Post {}".format(str(about.id)))
		self.assertEquals(length, 1000)
		self.assertTrue(blank)
		self.assertTrue(null)

	def test_second_content(self):
		about = AboutPage.objects.get(id=self.obj_id)
		blank = about._meta.get_field("second_content").blank
		null = about._meta.get_field("second_content").null

		self.assertTrue(blank)
		self.assertTrue(null)

	def test_image_of_second_content(self):
		about = AboutPage.objects.get(id=self.obj_id)
		blank = about._meta.get_field("image_of_second_content").blank
		null = about._meta.get_field("image_of_second_content").null
		upload = about._meta.get_field("image_of_second_content").upload_to
		image_file = "Blogapp/images/"

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(upload, image_file)

class TestRecentEvents(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.obj_id = RecentEvents.objects.create(name_of_event="my event").pk
		cls.recent = RecentEvents.objects.get(id=cls.obj_id)



	def test_name_of_event(self):

		length = self.recent._meta.get_field('name_of_event').max_length
		blank = self.recent._meta.get_field('name_of_event').blank
		null = self.recent._meta.get_field('name_of_event').null

		self.assertEquals(self.recent.__str__(), "Event {}".format(str(self.recent.id)))
		self.assertEquals(self.recent._meta.verbose_name_plural, "Recent Events")
		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 1000)


	def test_about_event(self):
		recent = RecentEvents.objects.get(id=self.obj_id)
		verbose = recent._meta.get_field('about_event').verbose_name
		blank = recent._meta.get_field('about_event').blank
		null = recent._meta.get_field('about_event').null

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(verbose, "Write about Event")

	def test_image_of_event(self):
		recent = RecentEvents.objects.get(id=self.obj_id)
		blank = recent._meta.get_field("image_of_event").blank
		null = recent._meta.get_field("image_of_event").null
		upload = recent._meta.get_field("image_of_event").upload_to
		image_file = "Blogapp/images/"

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(upload, image_file)

class TestHelp(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.obj_id = Help.objects.create(name="little child").pk
		cls.help_ = Help.objects.get(id=cls.obj_id)


	def test_string_method(self):
		str_method = self.help_.__str__()
		str_field = self.help_.name
		self.assertEquals(str_method, (str((str_field).title() + "'s " + "Story")))


	def test_image(self):
		upload = self.help_._meta.get_field("image").upload_to
		blank = self.help_._meta.get_field("image").blank
		null = self.help_._meta.get_field("image").null

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(upload, "Blogapp/images")

	def test_class_meta(self):
		verbose = self.help_._meta.verbose_name_plural
		order = self.help_._meta.ordering
		negative_id = ['-id']

		self.assertEqual(verbose, "Help The Little Children")
		self.assertEqual(order, negative_id)


	def test_name(self):
		blank = self.help_._meta.get_field('name').blank
		null = self.help_._meta.get_field('name').null
		length = self.help_._meta.get_field('name').max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 400)

	def test_child_story(self):
		blank = self.help_._meta.get_field('child_story').blank
		null = self.help_._meta.get_field('child_story').null

		self.assertEquals( self.help_._meta.get_field('child_story').verbose_name, "child's story")


		self.assertTrue(blank)
		self.assertTrue(null)


class TestTeam(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.obj_id = Team.objects.create(name="Jane Joe").pk
		cls.team = Team.objects.get(id=cls.obj_id)

	def test_class_meta(self):
		meta_verbose_ = self.team._meta.verbose_name_plural
		self.assertEquals(meta_verbose_, "Our Team")

	def test_team_image(self):
		upload = self.team._meta.get_field("team_image").upload_to
		blank = self.team._meta.get_field("team_image").blank
		null = self.team._meta.get_field("team_image").null

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(upload, "images/gallery/")

	def test_name(self):
		blank = self.team._meta.get_field("name").blank
		null = self.team._meta.get_field("name").null
		length = self.team._meta.get_field('name').max_length

		self.assertEquals(self.team.__str__(), self.team.name)
		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_position(self):
		blank = self.team._meta.get_field("position").blank
		null = self.team._meta.get_field("position").null
		length = self.team._meta.get_field('position').max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_facebook_url(self):
		blank = self.team._meta.get_field("facebook_url").blank
		null = self.team._meta.get_field("facebook_url").null
		length = self.team._meta.get_field("facebook_url").max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_twitter_url(self):
		blank = self.team._meta.get_field("twitter_url").blank
		null = self.team._meta.get_field("twitter_url").null
		length = self.team._meta.get_field("twitter_url").max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_instagram_url(self):
		blank = self.team._meta.get_field("instagram_url").blank
		null = self.team._meta.get_field("instagram_url").null
		length = self.team._meta.get_field("instagram_url").max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_pinterest_url(self):
		blank = self.team._meta.get_field("pinterest_url").blank
		null = self.team._meta.get_field("pinterest_url").null
		length = self.team._meta.get_field("pinterest_url").max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)

	def test_linkedin_url(self):
		blank = self.team._meta.get_field("linkedin_url").blank
		null = self.team._meta.get_field("linkedin_url").null
		length = self.team._meta.get_field("linkedin_url").max_length

		self.assertTrue(blank)
		self.assertTrue(null)
		self.assertEquals(length, 255)


	class TestTestimony(TestCase):

		@classmethod
		def setUpTestData(cls):
			cls.obj_id = Testimonial.objects.create(testimony="This is good").pk
			cls.testimony = Testimonial.objects.get(id=cls.obj_id)

		def test_testifier_image(self):
			upload = self.testimony._meta.get_field("testifier_image").upload_to
			self.assertEquals(upload, "images/Testimony")

		def test_testifier_name(self):
			length = self.testimony._meta.get_field("testifier_name").max_length
			self.assertEquals(length, 100)

		def test_remark(self):
			length = self.testimony._meta.get_field("remark").max_length
			default_val = self.testimony._meta.get_field("remark").default

			self.assertEquals(default_val, "")
			self.assertEquals(length, 100)

		def test_testimony(self):
			length = self.testimony._meta.get_field("testimonies").max_length
			self.assertEquals(length, 1000)
			
