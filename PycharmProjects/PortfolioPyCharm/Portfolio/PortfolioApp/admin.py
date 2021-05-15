from django.contrib import admin

from .models import BlogPost, Project, Contact

admin.site.register(BlogPost)
admin.site.register(Project)
admin.site.register(Contact)
