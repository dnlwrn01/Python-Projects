from django.db import models
from multiselectfield import MultiSelectField

PostTypes = [('Software', 'Software'), ('Hardware', 'Hardware'),
             ('Project Management', 'Project Management'), ('Lifestyle', 'Lifestyle')]


class BlogPost(models.Model):
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    type = models.CharField(max_length=25, choices=PostTypes, default=' ')
    title = models.CharField(max_length=50, default=' ')
    subTitle = models.CharField(max_length=50, default=' ')
    content = models.TextField()


    def __str__(self):
        return self.title + ' | ' + str(self.date)


languageUsed = [('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'), ('Python', 'Python'),
                ('Java', 'Java'), ('C#', 'C#'), ('C++', 'C++'), ('Objective-C', 'Objective-C'),
                ('PHP', 'PHP'), ('Ruby', 'Ruby'), ('SQL', 'SQL')]

frameworkUsed = [('Bootstrap', 'Bootstrap'), ('Django', 'Django'), ('React', 'React'),
                 ('jQuery', 'jQuery')]

databaseUsed = [('MySQL', 'MySQL'), ('MongoDB', 'MongoDB'), ('Oracle', 'Oracle')]

IDEUsed = [('VSCode', 'VSCode'), ('Atom', 'Atom'), ('PyCharm', 'PyCharm')]


class Project(models.Model):
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    IDE = MultiSelectField(max_length=25, choices=IDEUsed, default=' ')
    language = MultiSelectField(max_length=25, choices=languageUsed, default=' ')
    framework = MultiSelectField(max_length=25, choices=frameworkUsed, default=' ', blank=True)
    database = MultiSelectField(max_length=25, choices=databaseUsed, default=' ')
    title = models.CharField(max_length=50, default=' ')
    subTitle = models.CharField(max_length=50, default=' ')
    image1 = models.ImageField(upload_to='static/img/upload/')
    image2 = models.ImageField(upload_to='static/img/upload/')
    image3 = models.ImageField(upload_to='static/img/upload/')
    image4 = models.ImageField(upload_to='static/img/upload/')
    content = models.TextField(default=' ')
    purpose = models.TextField(default=' ')
    outcome = models.TextField(default=' ')
    reflection = models.TextField(default=' ')


    def __str__(self):
        return self.title + ' | ' + str(self.date)



class Contact(models.Model):
    name = models.CharField(max_length=25, default=' ')
    email = models.EmailField(default=' ')
    phone = models.CharField(max_length=13, default=' ')
    resumePDF = models.FileField(default=' ')
    resumeIMG = models.ImageField(default=' ')


    def __str__(self):
        return self.name + ' | ' + str(self.email)


