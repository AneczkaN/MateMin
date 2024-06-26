# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Task, Article
from .forms import TaskForm, CommentForm, ArticleCommentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def home(request):
    articles = Article.objects.all()
    return render(request, 'core/home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.all()

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = ArticleCommentForm()

    context = {
        'form': form,
        'comments': comments,
        'article': article
    }
    return render(request, 'core/article_detail.html', context)

# cała logika kalkulatora jest obsługiwana przez static/core/js/calculator.js
def calculator(request):
    return render(request, 'core/calculator.html')


def educational_links(request):
    links = [
        {'title': '3Blue1Brown', 'url': 'https://www.youtube.com/@3blue1brown', 'image': "https://yt3.googleusercontent.com/ytc/AIdro_nFzZFPLxPZRHcE3SSwzdrbuWqfoWYwLAu0_2iO6blQYAU=s176-c-k-c0x00ffffff-no-rj"},
        {'title': 'MateMaks', 'url': 'https://www.matemaks.pl/', 'image': "https://yt3.googleusercontent.com/ytc/AIdro_lTM7S-XUuqMFC4sDyVmsGko8WX-GtDzLVlgZN_PsAu8fM=s176-c-k-c0x00ffffff-no-rj"},
        {'title': 'Numberphile', 'url': 'https://www.youtube.com/@numberphile', 'image': "https://yt3.googleusercontent.com/ytc/AIdro_nmbQSAGKk1OZCBBf_sPJqLoFfYOVDWRDzALocBjGQtHeI=s176-c-k-c0x00ffffff-no-rj"},
        {'title': 'Veritasium', 'url': 'https://www.youtube.com/@veritasium', 'image': "https://yt3.googleusercontent.com/ytc/AIdro_nSatGjGLZG1_O1ztYxuKvRazCbk9A0kPhtt2NxEH4ZKfA=s176-c-k-c0x00ffffff-no-rj"},
    ]
    return render(request, 'core/educational_links.html', {'links': links})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'core/add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'core/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.task = task
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()

    return render(request, 'core/task_detail.html', {'task': task, 'comments': comments, 'form': form})
