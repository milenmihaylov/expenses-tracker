from django.contrib import admin

from expenses_tracker.expenses_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass
