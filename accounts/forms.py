from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'rasm', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'