from django.shortcuts import render, get_object_or_404

from .models import Professor

def detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    return render(request, 'professor/detail.html', {
        'professor': professor
    })