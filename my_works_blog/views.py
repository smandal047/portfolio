from django.shortcuts import render
from my_works_blog.models import Project, Post
from django.utils.text import slugify


def my_works(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'my_works.html', context)


def my_works_detail(request, pk):
    # project = Project.objects.filter(title=slug)
    project = Project.objects.get(pk=pk)
    posts = Post.objects.filter(related_project__exact=project)

    context = {
        'project': project,
        'posts': posts,
    }
    return render(request, 'my_works_detail.html', context)


def my_post_detail(request, pk, pk1):
    post = Post.objects.get(pk=pk1)

    context = {
        'post': post,
    }
    return render(request, 'my_post_detail.html', context)