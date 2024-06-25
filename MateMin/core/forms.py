# core/forms.py
from django import forms
from .models import Task, Comment, ArticleComment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']