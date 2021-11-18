from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import  CreateView
from django.shortcuts import render


User = get_user_model()

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/login.html"
    extra_context = {"action": "SIGN UP"}
    success_url = reverse_lazy("charts")

    def form_valid(self, form):
        form = form.save()
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.clean_password2(),
        )
        login(self.request, user)
        return super().form_valid(form)

def SimpleCharts(request):
    return render(request,"simplecharts.html")