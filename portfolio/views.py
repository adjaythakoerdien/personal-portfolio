from django.shortcuts import render
from .models import Testimonial, Vaardigheid_web, Vaardigheid_data, Vaardigheid_overig, Intro
from blog.models import Blogpost
from projects.models import Project
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os

# Create your views here.
def home(request):

    intro = Intro.objects.all()
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all().filter(uitgelicht=True)
    blogs = Blogpost.objects.order_by('-date')[:2]
    vaardigheid_web = Vaardigheid_web.objects.all()
    vaardigheid_data = Vaardigheid_data.objects.all()
    vaardigheid_overig = Vaardigheid_overig.objects.all()

    # lijst = []
    # for project in projects:
    #     lijst.append(str(project.technologies).split(', '))

    return render(request, 'portfolio/home.html',{
        'intro':intro,'testimonials':testimonials,'projects':projects,'blogs':blogs, 'pagina': 'home',
        'vaardigheid_web':vaardigheid_web, 'vaardigheid_data':vaardigheid_data, 'vaardigheid_overig':vaardigheid_overig
        }
        )
def send_gmail(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)

        send_mail(
            name,
            message,
            email,
            ['a.thakoerdien@gmail.com'],
            fail_silently=False,
        )

        verzonden = "Je berichtje is verzonden!"
        return render(request, 'portfolio/contact.html', {'pagina': 'contact', 'verzonden':verzonden})
    else:
        return render(request, 'portfolio/contact.html', {'pagina': 'contact',
                                                          'verzonden':'Er ging iets mis, probeer het opnieuw..'})

def contact(request):
    return render(request, 'portfolio/contact.html', {'pagina': 'contact'})
