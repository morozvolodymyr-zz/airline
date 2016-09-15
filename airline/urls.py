from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from airline_app.admin_views import users_list, delete_user
from airline_app.views import RegistrationView, LoginView, GetUsersView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^registration$', RegistrationView.as_view()),
    url(r'^registration_handler$', RegistrationView.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^login_handler$', LoginView.as_view()),
    url(r'^admin$', TemplateView.as_view(template_name='admin.html')),
    url(r'^get_users_list$', GetUsersView.as_view()),
    url(r'^users_list$', users_list),
    url(r'^delete_user/([\w]+)$', delete_user)
]