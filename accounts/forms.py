from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomRegistrationModel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomRegistrationModel
        fields = UserCreationForm.Meta.fields + ("email", "age",)
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomRegistrationModel
        fields = UserChangeForm.Meta.fields
