from expenses_tracker.expenses_profile.models import Profile
from expenses_tracker.expenses_tracker.models import Expense


def money_left():
	start_money = Profile.objects.first().budget
	expenses = 0
	for exp in Expense.objects.all():
		expenses += exp.price
	return start_money - expenses
