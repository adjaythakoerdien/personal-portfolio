from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)
    uitgelicht = models.BooleanField(default=False)

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

class Intro(models.Model):
    name =  models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/", default='static/portfolio/assets/images/profile.jpg')

    def __str__(self):
        return self.name

class Vaardigheid_web(models.Model):
    vaardigheid = models.CharField(max_length=250)

    def __str__(self):
        return self.vaardigheid

class Vaardigheid_data(models.Model):
    vaardigheid = models.CharField(max_length=250)

    def __str__(self):
        return self.vaardigheid

class Vaardigheid_overig(models.Model):
    vaardigheid = models.CharField(max_length=250)

    def __str__(self):
        return self.vaardigheid