from django.db import models

class Intro(models.Model):
    name =  models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/", default='static/portfolio/assets/images/profile.jpg')

    def __str__(self):
        return self.name

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="portfolio/images/", default='portfolio/images/project-figure-main1.png')
    image_2 = models.ImageField(upload_to="portfolio/images/", blank=True,
                                default='portfolio/images/project-figure-main1.png')

    def __str__(self):
        return self.title
