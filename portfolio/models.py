from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="portfolio/images/")

    def __str__(self):
        return self.name
