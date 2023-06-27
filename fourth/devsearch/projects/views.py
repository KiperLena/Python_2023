from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm #импорт формы
from django.contrib.auth.decorators import login_required #декаратор чтобы не заходили на страницы не зарегистрированные


def projects(request):
    pr = Project.objects.all()
    context = {
        'projects': pr
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile #в профайл выгружает профиль конкретный
    form = ProjectForm() #экземпляр класса

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid(): #если поля заполнены , введено все как надо
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')


    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile  # в профайл выгружает профиль конкретный
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)  # экземпляр класса

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


def delete_project(request, pk):
    profile = request.user.profile  # в профайл выгружает профиль конкретный
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete.html', context)


