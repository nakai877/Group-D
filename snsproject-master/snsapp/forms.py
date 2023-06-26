from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)

