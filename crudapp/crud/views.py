from django.shortcuts import render, get_object_or_404

from .models import Programming
from .forms import ProgrammingForm

def create(request):
    form = ProgrammingForm(request.POST or None, request.FILES or None)
    template_name = 'crud/create.html'
    context = {'form' : form}
    return render(request, template_name, context)

def list(request):
    qs = Programming.objects.all()
    context = {'object_list' : qs}
    return render(request, 'crud/list.html', context)


def detail(request, slug):
    obj = get_object_or_404(Programming, slug=slug)
    template_name = 'crud/detail.html'
    context = {"detail" : obj}
    return render(request, template_name, context)