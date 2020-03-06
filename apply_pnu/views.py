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
    all_user = ApplyForm.objects.all()

    for i in all_user:
        i.delete()
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



# def profile(request):
#     profile = Profile.objects.filter(user_id=request.user)
    
#     return render(request, 'profile.html', {'profile': profile})

class PnuLogin(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        # 프로필이 업데이트 되지 않은 회원은 업데이트 화면으로 리다이렉션 
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
    #     if self.request.user.is_authenticated:
    #         if self.request.user.profile.nickname == "":
    #             return redirect('profile_update')
    #         else:
    #             self.object = None        
    #             return super().get(request, *args, **kwargs)
    #     else:
    #         return redirect('login_main')


# from django.urls import reverse
# class CommunityUpdate(UpdateView):
#     model = CommunityPost
#     form_class = CommunityPostForm
#     template_name = 'community_create.html'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if self.object.author == self.request.user.profile:
#             return super().get(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     def get_success_url(self):
#         return reverse('community_detail', kwargs={
#             'pk': self.object.pk,
#         })
    
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
  
