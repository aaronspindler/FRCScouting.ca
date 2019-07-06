from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Blog

def blogs(request):
    blogs = Blog.objects
    return render(request, 'Blog/blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/detail.html',{'blog':detailblog})
