
import logging

from rest_framework.renderers import JSONRenderer
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django_airavata.apps.api.views import ProjectViewSet

logger = logging.getLogger(__name__)

@login_required
def experiments_list(request):
    request.active_nav_item = 'experiments'
    return render(request, 'django_airavata_workspace/experiments_list.html')

@login_required
def dashboard(request):
    request.active_nav_item = 'dashboard'
    return render(request, 'django_airavata_workspace/dashboard.html')

@login_required
def projects_list(request):
    request.active_nav_item = 'projects'

    response = ProjectViewSet.as_view({'get': 'list'})(request)
    projects_json = JSONRenderer().render(response.data)

    return render(request, 'django_airavata_workspace/projects_list.html', {
        'projects_data': projects_json
    })

@login_required
def create_experiment(request, app_module_id):
    request.active_nav_item = 'dashboard'

    return render(request, 'django_airavata_workspace/create_experiment.html', {
        'app_module_id': app_module_id
    })
