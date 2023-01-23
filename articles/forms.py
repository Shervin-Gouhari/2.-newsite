from django import forms
from .models import Comment, Article

class CommentForm(forms.ModelForm):
    class Meta:
        # model = Comments
        # fields = ["writer", "comment", "article"]
        # widgets = {
        #     "writer": forms.HiddenInput(),
        #     "article": forms.HiddenInput(),
        # }
        model = Comment
        fields = ["comment",]
        

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body",)