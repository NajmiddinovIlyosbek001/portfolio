from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from blog import filters
from blog.models import Category, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.filters import PostFilter, UserFilter
from blog.forms import PostForm
from accounts.models import CustomUser

class Home(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        kwargs['filter'] = PostFilter(self.request.GET, queryset=Post.objects.all())
        kwargs['posts'] = kwargs['filter'].qs
        return super().get_context_data(**kwargs)

@login_required
def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)

@login_required
def PostDelete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user == post.author:
        post.delete()
        return redirect('/')
        
@login_required
def PostDetail(request, slug, year, month, day, hour, minut, second):
    post = get_object_or_404(Post, slug=slug, created__year=year, created__month=month, created__day=day, created__hour=hour, created__minute=minut, created__second=second)
    context = {
        'i': post,
    }
    return render(request, 'post.html', context)

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user)
    context = {
        'us':user,
        'posts':posts,
    }
    return render(request, 'profile.html', context)

@login_required
def users(request):
    filter = UserFilter(request.GET, queryset=CustomUser.objects.all())
    users = filter.qs
    context = {
        'users': users,
        'filter': filter,
    }
    return render(request, 'users.html', context)