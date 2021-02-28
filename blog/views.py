from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def all_blogs(request):
    blogs = Blogpost.objects.order_by('-date')[:5]
    laatsteblog = Blogpost.objects.order_by('-date')[0]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs,'laatsteblog':laatsteblog})

def detail(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
