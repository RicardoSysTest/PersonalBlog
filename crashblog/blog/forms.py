from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    #Class Meta is used for Configuration
    class Meta:
        model = Comment
        fields = ('name','email','body')