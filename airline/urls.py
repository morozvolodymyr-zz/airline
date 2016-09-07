from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from airline_app.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^registration$', RegistrationView.as_view())
]
