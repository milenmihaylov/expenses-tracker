from expenses_tracker.expenses_profile.models import Profile
from expenses_tracker.expenses_tracker.models import Expense


def money_left():
	start_money = Profile.objects.first().budget
	expenses = Expense.objects.all()
	return start_money - sum(exp.price for exp in expenses)
