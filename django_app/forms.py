from django import forms
from .models import Post

class UppercaseCharField(forms.CharField):
    def to_python(self, value):
        return value.upper()

class PostForm(forms.ModelForm):
    title = UppercaseCharField(max_length=200)

    class Meta:
        model = Post
        fields = ["title","text","photo"]
