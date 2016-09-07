from django.shortcuts import render
from django.views.generic import FormView
from airline_app.forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
