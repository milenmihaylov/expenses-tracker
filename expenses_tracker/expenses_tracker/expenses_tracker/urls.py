from django.urls import path

from expenses_tracker.expenses_tracker.views import home_page, edit_expense, create_expense, delete_expense

urlpatterns = [
	path('', home_page, name='home page'),
	path('create/', create_expense, name='create expense'),
	path('edit/<int:pk>/', edit_expense, name='edit expense'),
	path('delete/<int:pk>/', delete_expense, name='delete expense'),
]
