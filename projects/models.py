from django.db import models
from datetime import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(default=datetime.now, blank=True)
    text = models.TextField()
    technologies = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.TextField(blank=True, max_length=250)
    uitgelicht = models.BooleanField(default=False)

    def __str__(self):
        return self.title