# core/admin.py

from django.contrib import admin
from .models import Task, Comment, Article, ArticleComment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sources', 'authors')
    search_fields = ('title', 'content', 'sources', 'authors')
    list_filter = ('authors',)

@admin.register(ArticleComment)
class CommentArticleAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)