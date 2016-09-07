from django import forms
from airline_app.models import Users


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=Users.max_len_name)
    surname = forms.CharField(max_length=Users.max_len_name)
    e_mail = forms.EmailField()
    password = forms.CharField(max_length=Users.max_len_pass, widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=['adm', 'dis'])
