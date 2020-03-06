from django.forms import ModelForm
from .models import ApplyForm

class ApplyFormForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update(
        #     {'placeholder': "제목",
        #      'class': 'enroll_title',
        #      'autocomplete':'off'})
        # self.fields['body'].widget.attrs.update(
        #     {'placeholder': '새로 만나게 될 딩가육아 동지에게 간단한 소개를 적어주세요!',
        #      'class': 'enroll_body',})
        

    class Meta:
        model = ApplyForm
        fields = ('inroduce', 'position', 'goal', 'plan','team','concept','portfolio','interview','experience','schedule',)
        