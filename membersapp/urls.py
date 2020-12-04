from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from .forms import *

urlpatterns = [
	re_path(r'^profile/(?P<username>[.@_+\w-]+)$', views.user_profile, name='profile'),
	path('register/', views.UserRegistrationView.as_view(), name='register'),
	path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
	path('password_success/', views.password_success, name='password_success'),
	path('edit_pasword/password/', views.PasswordsChangeView.as_view(template_name='registration/change_password.html')),
	re_path('edit_profile/<int:pk>/', views.UserEditView.as_view(), name='edit_profile'),
	path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
	#path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name="password_reset"),
	path('password-reset/', views.PassWordResettingView.as_view(), name="password_resett"),
	path('password-reset/done',
		auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_resett_done"),
	path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

	path('password-reset/complete',
		auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_resett_complete"),

]
