from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile,ApplyForm
from .forms import RegisterForm, ProfileForm, LoginForm
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import ApplyFormForm
# Create your views here.
def index(request):
    
    return render(request, 'index.html')



def signup(request):
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


class PnuLogin(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        if not self.request.user.profile.name:    
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



# def apply(request):

#     if request.method =="POST":
#         temp_form = ApplyFormForm(request.POST)
#         if temp_form.is_valid():
#             print("밸리드")
#             print(request.POST)
#             temp_form.save()
#             print(temp_form)
#             return redirect('index')
#         else:
#             print("낫밸리드")
#             return redirect('apply')
#     else:
        
#         return render(request, 'apply.html', {'form': ApplyFormForm()})
class Apply(CreateView):
    form_class = ApplyFormForm
    template_name = 'apply.html'
    success_url = reverse_lazy('index')


    

@method_decorator(user_passes_test(lambda u: u.is_superuser), name="get")
class ApplyList(ListView):
    template_name="apply_list.html"
    context_object_name = "apply_all"
    model = ApplyForm
# def get(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             if self.request.user.profile.nickname == "":
#                 return redirect('profile_update')
#             else:
#                 self.object = None        
#                 return super().get(request, *args, **kwargs)
#         else:
#             return redirect('login_main')


class ApplyDetail(DetailView):
    model = ApplyForm
    template_name = "apply_detail.html"
    context_object_name = "apply_one"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(self, request)
        
        if kwargs['pk'] == request.user.profile.applyform.id:
            return super().get(self, request)
        else:
            return redirect('index')



class ApplyEdit(UpdateView):
    form_class = ApplyFormForm
    template_name = 'apply.html'
    model = ApplyForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if kwargs['pk'] == request.user.profile.applyform.id:
            return super().get(self, request)
        else:
            return redirect('index')

    def post(self, request, *args, **kwargs):
        if kwargs['pk'] == request.user.profile.applyform.id:
            return super().get(self, request)
        else:
            return redirect('index')
# from django.urls import reverse_lazy
# class CommunityDelete(DeleteView):
#     model = CommunityPost
#     template_name = 'community_detail.html'
#     success_url = reverse_lazy('community')

#     def post(self, request, *args, **kwargs):
#         if self.request.user.profile == self.get_object().author:
#             return self.delete(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
    



def profile_update(request):
    user = request.user
    profile = user.profile
    
    profileform = ProfileForm(request.POST or None, instance=profile)

    context = {'profileform': profileform,
                    'profile': profile}

    if request.method == 'POST':
        if profileform.is_valid():
            profile.save()  
            print("세이브야!")
            return redirect('index')
        
        else:
            return render(request, 'profile_update.html', context)

            
    profileform = ProfileForm(instance=profile)
    context = {'profileform': profileform, 'profile':profile}
    

    return render(request, 'profile_update.html', context)
  
