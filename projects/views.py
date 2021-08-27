from django.shortcuts import render
from .models import Project

# Create your views here.
def all_projects(request):
	projects = Project.objects.all()

	return render(request, 'projects/projects.html', {'projects':projects})

def project(request):
	# project = get_object_or_404(Project, pk=project_id)

	return render(request, 'projects/project.html')
