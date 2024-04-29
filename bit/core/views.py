from django.shortcuts import render
from group.models import Group
from professor.models import Professor

def index(request):
    groups = Group.objects.all()
    professors = Professor.objects.all() 
    return render(request, 'core/index.html', {
        'groups': groups, 
        'professors': professors,
        })
