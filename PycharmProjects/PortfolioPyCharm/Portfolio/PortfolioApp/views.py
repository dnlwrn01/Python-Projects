from django.shortcuts import render
from .models import Project, BlogPost
import os


def home(request):

    Project.image1 = str(Project.image1)[10:]
    cards = Project.objects.all()
    content = {'cards': cards}
    return render(request, 'portfolio/index.html', content)


def projects(request):
    cards = Project.objects.all()
    content = {'cards': cards}
    return render(request, 'portfolio/projects.html', content)


def blog(request):
    posts = BlogPost.objects.all()
    content = {'posts': posts}
    return render(request, 'portfolio/blog.html', content)


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')



