from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
from account.forms import LoginForm , RegisterationForm
from django.contrib.auth.models import User
from mixins import LoginRequirdMixins

class LoginView(LoginRequirdMixins , FormView):
    template_name = 'account/log.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:main')
    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request , username=cd['username'] , password=cd['password'])
        if user is not None:
            login(self.request , user)
            return HttpResponse('you are login the site')
        else:
            return redirect(reverse_lazy('account:login'))
        
class Register(LoginRequirdMixins , FormView):
    template_name = 'account/register.html'
    form_class = RegisterationForm
    success_url = reverse_lazy('home:main')
    def form_valid(self, form):
        cd = form.cleaned_data
        username = cd['username']
        password = cd['password']
        password2 = cd['password2']
        user = User.objects.create_user(username=username , password=password)
        login(self.request , user)
        return redirect('home:main')        

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:main')
    else:
        return redirect('home:main')