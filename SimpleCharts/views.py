from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render


User = get_user_model()

class SigninForm(UserCreationForm):
    pass


class SignUpView(CreateView):
    form_class = SigninForm
    template_name = "registration/login.html"
    extra_context = {"action": "SIGN UP"}
    success_url = reverse_lazy("charts")

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

def SimpleCharts(request):
    return render(request,"simplecharts.html")

def start(request):
    return render(request,"start.html")