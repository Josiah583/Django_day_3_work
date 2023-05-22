from django import forms
from .models import Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class SignupForm(form.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'address', 'phone_number')
        exlude = ('is_verifed', 'is_admin', 'is_staff', 'is_seller')