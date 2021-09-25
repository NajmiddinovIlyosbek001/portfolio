from django.shortcuts import render
from accounts.forms import CustomUserCreationForm
from django.urls.base import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')