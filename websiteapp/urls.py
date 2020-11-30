from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('contact/', views.contact, name="contact"),
	path('activity/', views.activity, name="gallery"),
	path('team/', views.TeamView.as_view(), name="team"),
	path('about/', views.about, name="about"),
	path('help,<int:pk>/', views.help, name="help"),
	path('form-submitted/', views.submitted_form, name='submitted_form')


]
