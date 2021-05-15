from django.shortcuts import render
from .models import BlogPost, Project, Contact


def home(request):

    return render(request, 'portfolio/index.html')


def projects(request):
    card = Project.objects.all()
    context = {'card': card}
    return render(request, 'portfolio/projects.html', context)


def blog(request):
    return render(request, 'portfolio/blog.html')


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')

