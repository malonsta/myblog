from django import forms
from myblog.models import Contact
from django.forms import ModelForm


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'YourName'
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment!'
        })
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
