from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    email    = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
     
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
