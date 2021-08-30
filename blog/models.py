from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="portfolio/images/", default='portfolio/images/project-figure-main1.png')
    image_2 = models.ImageField(upload_to="portfolio/images/", blank=True,
                                default='portfolio/images/project-figure-main1.png')

    def __str__(self):
        return self.title
