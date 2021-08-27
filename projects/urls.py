from django.urls import include, path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:project_id>/', views.project, name='project'),
    ]
