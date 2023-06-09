from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def index_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        'title': 'DjangoBlog',
        'posts': posts,
    }
    return render(request=request, template_name='blogs/index.html', context=context)


def create_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    else:
        form = PostForm()
    context = {
        'title': 'DjangoBlog - Create Post',
        'form': form,
    }
    return render(request=request, template_name='blogs/create.html', context=context)


def get_post_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(klass=Post, pk=pk)
    context = {
        'title': f'DjangoBlog - {post.title}',
        'post': post,
    }
    return render(request=request, template_name='blogs/post.html', context=context)


def post_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    current_post = get_object_or_404(klass=Post, pk=pk)
    form = PostForm(instance=current_post)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=current_post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {
        'title': f'DjangoBlog - {current_post.title}',
        'post': current_post,
        'form': form,
    }
    return render(request=request, template_name='blogs/edit.html', context=context)
