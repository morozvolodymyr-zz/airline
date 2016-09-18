from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from airline_app.forms import RegistrationForm, LoginForm
from airline_app.models import Users


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return render(request, 'index.html', {})

        return render(request, 'registration.html', {'error': 'error in registration', 'form': RegistrationForm})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.session.get('user_e_mail') is not None:
            u = Users.objects.filter(e_mail=request.session.get('user_e_mail')).first()
            if u.id_role_id == 1:
                # return redirect(to='admin', e_mail=u.e_mail, name=u.name, surname=u.surname)
                return render(request, 'admin.html', {'e_mail': u.e_mail, 'name': u.name, 'surname': u.surname})
            # redirect
            elif u.id_role_id == 2:
                return render(request, 'dispatcher.html', {'e_mail': u.e_mail, 'name': u.name, 'surname': u.surname})
            else:
                return render(request, 'user_flights.html', {'e_mail': u.e_mail, 'name': u.name, 'surname': u.surname})
        else:
            form = self.get_form(LoginView.form_class)
            return render(request, LoginView.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_e_mail = login_form.cleaned_data['e_mail']
            user_password = login_form.cleaned_data['password']
            u = Users.objects.filter(e_mail=user_e_mail, password=user_password).first()
            if u is not None:
                request.session['user_e_mail'] = user_e_mail
                if u.id_role_id == 1:
                    request.session['user_role'] = 1
                    return render(request, 'admin.html', {'e_mail': user_e_mail, 'name': u.name, 'surname': u.surname})
                elif u.id_role_id == 2:
                    request.session['user_role'] = 2
                    return render(request, 'dispatcher.html',
                                  {'e_mail': user_e_mail, 'name': u.name, 'surname': u.surname})
                else:
                    return render(request, 'user_flights.html',
                                  {'e_mail': user_e_mail, 'name': u.name, 'surname': u.surname})
            else:
                return render(request, 'login.html', {'error': 'login incorrect', 'form': LoginForm})


class GetUsersView(View):
    template_name = 'users_list.html'

    def get(self, request):
        return render(request, 'users_list.html', {})


class GetFlightsView(View):
    template_name = 'flights.html'

    def get(self, request):
        return render(request, 'flights.html', {})
