from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomRegistrationModel

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomRegistrationModel
    list_display = ["username", "email", "age", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age",)}),
    )
    
admin.site.register(CustomRegistrationModel, CustomUserAdmin)
