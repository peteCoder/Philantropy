from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.views.generic import ListView
from .models import Team, Testimonial, Gallery, AboutPage, Help, RecentEvents, ShortDiscriptionInAboutPage

from .forms import ContactForm

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#Start with this

def help(request, pk):
	help_child = get_object_or_404(Help, pk=pk)

	context = {
		"help_child": help_child,
	}
	return render(request, "Main/help_detail.html", context)

def home(request):
	testify = Testimonial.objects.all()
	help_child = Help.objects.all()
	about_page = AboutPage.objects.all()
	recent_activities = RecentEvents.objects.all()

	context = {
		'help_child': help_child,
		'abouts': about_page,
		'testify':testify,
		'recent_activities': recent_activities,
		}


	return render(request, 'Main/index.html', context)


def about(request):

	testify = Testimonial.objects.all()

	team_members = Team.objects.all()
	about_page = AboutPage.objects.all()
	short_abouts = ShortDiscriptionInAboutPage.objects.all()

	context = {
		'testify':testify,'abouts': about_page,
		'short_abouts': short_abouts,
		'team_members': team_members,
	}
	return render(request, 'Main/about.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			form.save()

			print("VALID")

			return redirect(reverse('submitted_form'))
	else:
		form = ContactForm()


	context = {
		'form': form,
	
	}

	return render(request, 'Main/contact.html', context)




# def activities(request):
# 	return render(request, 'Main/activity.html', {})


# def team(request):
# 	return render(request, 'Main/team.html', {})


def activity(request):
    gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, 'Main/activity.html', context)

class TeamView(ListView):
	model = Team
	template_name = 'Main/team.html'

	def get_context_data(self, *args, **kwargs):
		team_members = Team.objects.all()
		testify = Testimonial.objects.all()
	
		context = super(TeamView, self).get_context_data(*args, **kwargs)
		context['team_members'] = team_members
		context['testify'] = testify
	

		return context


@csrf_exempt
def submitted_form(request):
	return render(request, "Main/submitted_form.html", {})
