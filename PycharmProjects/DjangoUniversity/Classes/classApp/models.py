from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.IntegerField(default="000", blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default="00.0", blank=True, null=False)



    objects = models.Manager()

    def __str__(self):
        return self.title
