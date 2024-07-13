from django import forms

from .models import Post
from froala_editor.widgets import FroalaEditor

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            'content': FroalaEditor(),
        }