from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as AdminUserChangeForm
from django.contrib.auth.forms import UserCreationForm as AdminUserCreationForm

User = get_user_model()


class UserChangeForm(AdminUserChangeForm):
    class Meta(AdminUserChangeForm.Meta):
        model = User


class UserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')

    error_messages = {
        "duplicate_email": "A user with that email already exists.",
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages["duplicate_email"],
            code="duplicate_email",
        )
