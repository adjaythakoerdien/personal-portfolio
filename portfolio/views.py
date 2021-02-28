from django.shortcuts import render
from .models import Project, Testimonial
from blog.models import Blogpost

# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    blogs = Blogpost.objects.order_by('-date')[:2]
    lijst = ['Python', 'Django', 'Bootstrap', 'SQLite', 'HTML/CSS']

    return render(request, 'portfolio/home.html',
    {'testimonials':testimonials,'projects':projects,'blogs':blogs,'lijst':lijst})

def contact(request):
    return render(request, 'portfolio/contact.html')
