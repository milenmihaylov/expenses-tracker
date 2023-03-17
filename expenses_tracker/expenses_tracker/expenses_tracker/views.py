from django.shortcuts import render, redirect

from expenses_tracker.expenses_profile.models import Profile
from expenses_tracker.expenses_profile.views import create_profile
from expenses_tracker.expenses_tracker.forms import ExpenseForm
from expenses_tracker.expenses_tracker.models import Expense
from expenses_tracker.utils.utils import money_left


def home_page(request):
	profile = Profile.objects.first()
	if not profile:
		return create_profile(request)
	context = {
		'profile': profile,
		'expenses': Expense.objects.all(),
		'money_left': money_left(),
	}
	return render(request, 'home-with-profile.html', context)


def create_expense(request):
	if request.method == "GET":
		context = {'form': ExpenseForm()}
		return render(request, 'expense-create.html', context)
	form = ExpenseForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('home page')
	context = {'form': form}
	return redirect(request, 'expense-create.html', context)


def edit_expense(request, pk):
	expense = Expense.objects.get(pk=pk)
	form = ExpenseForm(initial=expense.__dict__)
	if request.method == 'GET':
		context = {'form': form}
		return render(request, 'expense-edit.html', context)
	form = ExpenseForm(request.POST, instance=expense)
	if form.is_valid():
		form.save()
		return redirect('home page')
	context = {'form': form}
	return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
	expense = Expense.objects.get(pk=pk)
	form = ExpenseForm(initial=expense.__dict__)
	if request.method == 'GET':
		context = {'form': form}
		return render(request, 'expense-delete.html', context)
	expense.delete()
	return redirect('home page')


