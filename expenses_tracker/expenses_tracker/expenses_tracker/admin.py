from django.contrib import admin

from expenses_tracker.expenses_tracker.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	pass
