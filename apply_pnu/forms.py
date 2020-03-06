from django.forms import ModelForm
from .models import ApplyForm

class ApplyFormForm(ModelForm):

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
        
