from django.shortcuts import render
from  django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.views.generic import CreateView
from cuentas.forms import RegistroForm
from django.core.urlresolvers import reverse_lazy



# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "form_registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home:home')
