from django.shortcuts import render, get_object_or_404
from .models import Project, Intro

# Create your views here.
def all_projects(request):
	projects = Project.objects.all()
	intro = Intro.objects.all()

	return render(request, 'projects/projects.html', {'projects':projects, 'intro':intro})

img_dict = {'html': 'portfolio/assets/images/webdev-icons/html5.svg',
			'django': 'portfolio/assets/images/webdev-icons/django.svg',
			'python': 'portfolio/assets/images/webdev-icons/python.svg',
			'bootstrap': 'portfolio/assets/images/webdev-icons/bootstrap4.svg',
			'tensorflow': 'portfolio/assets/images/webdev-icons/tensorflow-2.svg'
			}

def project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)


	lijst = str(project.technologies).split(', ')
	img_lijst = []

	for l in lijst:
		try:
			img_lijst.append(img_dict[l])
		except:
			img_lijst.append(img_dict['html'])

	return render(request, 'projects/project.html', {'project':project, 'img_lijst':img_lijst})
