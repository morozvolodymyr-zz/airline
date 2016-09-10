from django import forms
from django.forms import ModelChoiceField
from airline_app.models import Users, Roles


class MyModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.role


class RegistrationForm(forms.ModelForm):
    id_role = MyModelChoiceField(queryset=Roles.objects.all(), label='Role')

    class Meta:
        model = Users
        fields = ['name', 'surname', 'e_mail', 'password', 'id_role']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['e_mail', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
