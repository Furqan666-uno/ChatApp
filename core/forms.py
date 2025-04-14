from django.contrib.auth.forms import UserCreationForm # allows us to use Built In signup and login forms  
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'password1', 'password2'] # these fields are predefined for signUp forms 