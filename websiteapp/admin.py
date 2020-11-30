from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.site_header = "Gift A Child Initiative Administration"
admin.site.site_title = "Gift A Child Initiative Admin Portal"
admin.site.index_title = "Welcome to GACI Portal"

# Register your models here.
admin.site.register(AboutPage)
admin.site.register(Gallery)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Help)
admin.site.register(RecentEvents)
admin.site.register(ShortDiscriptionInAboutPage)
