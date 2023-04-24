from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/home.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {"project": project}
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_project.html", context)
