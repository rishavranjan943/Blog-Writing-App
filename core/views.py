from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.contrib import messages  
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    blogs=Blog.objects.all().order_by('published_date')
    search_blog=request.GET.get('search_blog')
    if search_blog!=' ' and search_blog is not None:
        blogs=blogs.filter(title__icontains=search_blog) | blogs.filter(description__icontains=search_blog)
    paginator=Paginator(blogs, 5)
    page_number=request.GET.get('page')
    blogs=paginator.get_page(page_number)
    return render(request, 'index.html',{
        'blogs':blogs
    })


def add_blog(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        author=request.user
        blog=Blog.objects.create(title=title,description=description,author=author)
        blog.save()
        messages.success(request, 'Blog added successfully')
        return redirect('core:index')
    return render(request, 'add_blog.html')


def detail_blog(request,id):
    blog=Blog.objects.get(id=id)
    return render(request, 'detail_blog.html',{
        'blog':blog
    })

@login_required(login_url='/login')
def my_blog(request):
    blogs=Blog.objects.filter(author=request.user)
    return render(request, 'my_blog.html',{
        'blogs':blogs
    })


@login_required(login_url='/login')
def update_blog(request,id):
    blog=Blog.objects.get(id=id)
    if blog.author != request.user:
        messages.info(request, 'You are not authorized to update this blog')
        return redirect('core:detail_blog', id=id)
    if request.method == 'POST':
        render(request, 'update_blog.html',{
        'blog':blog
        })
        blog.title=request.POST.get('title')
        blog.description=request.POST.get('description')
        blog.updated_date=datetime.now()
        blog.save()
        messages.success(request, 'Blog updated successfully')
        return redirect('core:my_blog')

@login_required(login_url='/login')
def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    if blog.author != request.user:
        messages.info(request, 'You are not authorized to delete this blog')
        return redirect('core:detail_blog',id=id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('core:my_blog')