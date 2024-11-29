from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .models import UserAuth

class UserAuthForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = UserAuth

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email address'

