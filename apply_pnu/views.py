from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from .forms import RegisterForm, ProfileForm, LoginForm
from django.conf import settings



# Create your views here.
def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user_instance = registerform.save(commit=False)
            user_instance.set_password(registerform.cleaned_data['password1'])
            user_instance.is_active = True
            user_instance.save()
            user=User.objects.get(username=registerform.cleaned_data['username'])
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile_update')
        else:
            registerform = RegisterForm(request.POST)
            return render(request, 'signup.html', {'RegisterForm': registerform})

    registerform = RegisterForm()
    return render(request, 'signup.html',{'RegisterForm':registerform})



def profile(request):
    profile = Profile.objects.filter(user_id=request.user)
    
    return render(request, 'profile.html', {'profile': profile})

class PnuLogin(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        # 프로필이 업데이트 되지 않은 회원은 업데이트 화면으로 리다이렉션 
        if not self.request.user.profile.nickname:    
            url = "/profile_update/"
            return url
        else:
        # 로그인한 현재 페이지로 연결
            # url = self.request.path
            url = "/"
            return url
        
        return resolve_url(settings.LOGIN_REDIRECT_URL)
   


def login(request):
    return render(request, 'login.html')
