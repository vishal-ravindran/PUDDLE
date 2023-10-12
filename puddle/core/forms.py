from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# for loggin in 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': "Please Enter your Username",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))
     
    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': "Please Enter your Password",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))


# for signing up
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': "Please Enter your Username",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))

    email = forms.CharField(widget=forms.EmailInput(attrs= {
        'placeholder': "Please Enter your Email address",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': "Please Enter your Password",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))
    password2 = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': "Please confirm your password",
        'class' : 'w-full px-6 py-4 rounded-xl'
    }
    ))
