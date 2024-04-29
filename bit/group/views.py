from django.shortcuts import render, get_object_or_404

from .models import Group

def detail(request, pk):
    group = get_object_or_404(Group, pk=pk)

    return render(request, 'group/detail.html', {
        'group': group
    })