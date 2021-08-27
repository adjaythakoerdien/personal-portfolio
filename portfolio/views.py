from django.shortcuts import render
from .models import Project, Testimonial, Vaardigheid_web, Vaardigheid_data, Vaardigheid_overig, Intro
from blog.models import Blogpost

# Create your views here.
def home(request):

    intro = Intro.objects.all()
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all().filter(uitgelicht=True)
    blogs = Blogpost.objects.order_by('-date')[:2]
    vaardigheid_web = Vaardigheid_web.objects.all()
    vaardigheid_data = Vaardigheid_data.objects.all()
    vaardigheid_overig = Vaardigheid_overig.objects.all()

    return render(request, 'portfolio/home.html',
    {'intro':intro,'testimonials':testimonials,'projects':projects,'blogs':blogs, 'pagina': 'home',
    'vaardigheid_web':vaardigheid_web, 'vaardigheid_data':vaardigheid_data, 'vaardigheid_overig':vaardigheid_overig})


def contact(request):

    return render(request, 'portfolio/contact.html', {'pagina': 'contact'})


def projects(request):

    projects = Project.objects.all()

    return render(request, 'portfolio/projects.html', {'projects': projects})