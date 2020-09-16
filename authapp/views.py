from django.shortcuts import render
from django.contrib.auth import login
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_type1_required, user_type2_required, user_type3_required


# Create your views here.
from django.shortcuts import redirect, render
from .forms import TeacherSignUpForm
from .models import User
from django.views.generic import CreateView


class SignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'
 
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

def home(request):
    return render(request, 'home.html')

@user_type1_required
def alpha(request):
    return render(request, 'alpha.html')

@user_type2_required
def bravo(request):
    return render(request, 'bravo.html')

@user_type3_required
def charli(request):
    return render(request, 'charli.html')

