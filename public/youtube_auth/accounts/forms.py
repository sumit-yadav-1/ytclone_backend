from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # if you have a Profile model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap classes
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control rounded-pill px-3 py-2',
            })