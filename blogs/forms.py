from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter title',
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter content',
        'rows': 5,
        'cols': 20,
    }))

    class Meta:
        model = Post
        fields = ['title', 'content']
