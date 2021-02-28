from django.shortcuts import render
from .models import Project, Testimonial
from blog.models import Blogpost

# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    blog1 = Blogpost.objects.order_by('-date')[0]
    blog2 = Blogpost.objects.order_by('-date')[1]
    blog3 = Blogpost.objects.order_by('-date')[2]
    blog4 = Blogpost.objects.order_by('-date')[3]
    lijst = ['Python', 'Django', 'Bootstrap', 'SQLite', 'HTML/CSS']

    return render(request, 'portfolio/home.html',
    {'testimonials':testimonials,'projects':projects,'blog1':blog1,'blog2':blog2,'blog3':blog3,'blog4':blog4,'lijst':lijst})
