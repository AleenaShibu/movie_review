from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form= CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email','username','age','is_staff' ,]

	fieldsets = (
		(None,{'fields':('email','password','age')}),
		('permissions',{'fields':('is_staff','is_active')}),
		)
	add_fieldsets = (
		(None, {'classes':('wide',),
			'fields':('email','password','password2','is_staff','is_active')
			}),
		)
			
admin.site.register(CustomUser,CustomUserAdmin)	