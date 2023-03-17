from django.shortcuts import render, redirect

from expenses_tracker.expenses_profile.forms import ProfileForm
from expenses_tracker.expenses_profile.models import Profile
from expenses_tracker.utils.utils import money_left


def profile_page(request):
	context = {
		'profile': Profile.objects.first(),
		'money_left': money_left(),
	}
	return render(request, 'profile.html', context)


def create_profile(request):
	if request.method == 'GET':
		context = {
			'form': ProfileForm(),
		}
		return render(request, 'home-no-profile.html', context)
	create_form = ProfileForm(request.POST)
	if create_form.is_valid():
		create_form.save()
		return redirect('home page')


def edit_profile(request):
	profile = Profile.objects.first()
	if request.method == 'GET':
		context = {
			'profile_form': ProfileForm(initial=profile.__dict__),
		}
		return render(request, 'profile-edit.html', context)
	else:
		form = ProfileForm(
			request.POST,
			instance=profile,
		)
		if form.is_valid():
			form.save()
			return redirect('profile page')
		context = {'form': form}
		return render(request, 'profile-edit.html', context)


def delete_profile(request):
	if request.method == 'GET':
		return render(request, 'profile-delete.html')
	Profile.objects.first().delete()
	return redirect('/')
