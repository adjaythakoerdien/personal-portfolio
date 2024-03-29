from django.db import models
from datetime import datetime

class Intro(models.Model):
    name =  models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(default=datetime.now, blank=True)
    intro = models.TextField(blank=True)
    text_list = models.TextField(blank=True)
    text = models.TextField()
    eind = models.TextField(blank=True)
    technologies = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    image_2 = models.ImageField(upload_to="portfolio/images/", blank=True, default='portfolio/images/project-figure-main1.png')
    image_3 = models.ImageField(upload_to="portfolio/images/", blank=True)
    url = models.TextField(blank=True, max_length=250)
    uitgelicht = models.BooleanField(default=False)

    def __str__(self):
        return self.title
