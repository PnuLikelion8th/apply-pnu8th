from .models import ApplyForm, Profile
from django import forms
from django.contrib.auth.models import User


class ApplyFormForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['introduce'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['position'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea', })

        self.fields['goal'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea', })

        self.fields['plan'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea', })

        self.fields['team'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['concept'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['portfolio'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['interview'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['experience'].widget.attrs.update(
            {'placeholder': "",
             'class': 'form-control custom_textarea',})

        self.fields['schedule'].widget.attrs.update(
                 {'placeholder': "",
                  'class': 'form-control custom_textarea', })

    
    class Meta:
        model = ApplyForm
        fields = ('introduce', 'position', 'goal', 'plan','team','concept','portfolio','interview','experience','schedule',)
        



class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='학번')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput())
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username']
        

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': '학번',
             'class': "rg_num",
             'id': "rg_search"})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': '비밀번호',
             'class': "rg_password",
             'id': "rg_pw"})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': '비밀번호확인',
             'class': "rg_password",
             'id': "rg_pw_con"})
    # def clean_username(self):
    #     username = self.cleaned_data.get('username', '')
    #     if username:
    #         if get_user_model().objects.filter(username=username).exists():
    #             raise ValidationError('이미 존재하는 이메일 아이디 입니다')
    #         if get_user_model().objects.filter(email=username).exists():
    #             raise ValidationError('소셜 가입된 이메일입니다.')
    #     return username

    def clean_password2(self):
        cleaned_password1 = self.cleaned_data.get('password1', '')
        cleaned_password2 = self.cleaned_data.get('password2', '')

        if cleaned_password1 != cleaned_password2:
            raise forms.ValidationError('두 비밀번호가 다릅니다.')
        # if not(5<len(cleaned_password1)<13):
        #     raise forms.ValidationError('비밀번호의 형식을 지켜주세요.')
        return cleaned_password1

    
class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': "pf_name",
             'id': "pf_name"})

        self.fields['major'].widget.attrs.update(
            {'placeholder': '학과',
             'id': "pf_major"})

        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': '010-0000-0000',
             'class': "pf_phone_number",
             'id': "pf_phone_number"})

        self.fields['email'].widget.attrs.update(
            {'placeholder': '이메일',
             'id': "pf_email"})

        self.fields['m_or_f'].widget.attrs.update(
            {'placeholder': '성별',
             'id': "pf_m_or_f",})
        
        
    class Meta:
        model = Profile
        fields = ['user','name', 'major', 'phone_number', 'email', 'm_or_f',]
    
    # def clean_nickname(self):
    #     # print(self)
    #     # print(f"forms.py clean_nickname 작동 : {self.cleaned_data}")
    #     nickname = self.cleaned_data.get('nickname', '')
    #     if nickname:
    #         if 1<len(nickname)<7:
    #             if Profile.objects.filter(nickname=nickname).exists():
    #                 # 자기 자신의 닉네임이면 pass
    #                 if self.cleaned_data.get('user').profile.nickname == nickname:
    #                     return nickname
    #                 else:
    #                     print("얘가 돌아가는건가")
    #                     raise ValidationError('이미 존재하는 닉네임 입니다.')
    #         else:
    #             raise ValidationError('2~6글자의 닉네임이어야 합니다.')
    #     else:
    #         raise ValidationError('닉네임을 입력해주세요.')
    #     return nickname


from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['username'].widget.attrs.update(
            {'class': "username_input",
             'placeholder': '학번',
             'autocomplete':"off"})
        
        self.fields['password'].label = ""
        self.fields['password'].widget.attrs.update(
            {'class': "password_input",
             'placeholder': '비밀번호',
             'autocomplete':"off"})
    
    error_messages = {
        'invalid_login': (
            "일치하는 아이디/비밀번호가 없습니다."
        ),
    }

    fields = ('introduce', 'position', 'goal', 'plan','team','concept','portfolio','interview','experience','schedule',)
        
