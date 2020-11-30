from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView

from django.urls import reverse_lazy
from .forms import SignUpForm, PasswordChangingForm, ProfilePageForm, EditProfileForm, PasswordResettingForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from .models import Profile
#from blogapp.models import Category
from django.contrib.auth.models import User

# Create your views here.

class CreateProfilePageView(CreateView):
	model = Profile
	form_class =  ProfilePageForm
	template_name = "registration/create_user_profile_page.html"


	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CreateProfilePageView, self).get_context_data(*args, **kwargs)
		return context

def user_profile(request, username):
    page_user = get_object_or_404(User, username=username)
    #cat_menu = Category.objects.all()
    context =  {
        'page_user': page_user.profile,
        #'cat_menu':cat_menu
    }
    return render(request, 'registration/user_profile.html', context)


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(*args, **kwargs)
        return context



class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        return context



class PasswordsChangeView(PasswordChangeView):
	form_class =  PasswordChangingForm
	success_url = reverse_lazy('password_success')

	def get_context_data(self, *args, **kwargs):
		context = super(PasswordsChangeView, self).get_context_data(*args, **kwargs)
		return context

def password_success(request):
	return render(request, 'registration/password_success.html', {})


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile_settings.html'
    success_url = reverse_lazy('blog_home')


    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        return context


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user

        return context


class PassWordResettingView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = PasswordResettingForm
