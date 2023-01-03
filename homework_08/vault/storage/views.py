from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from storage.models import Secret, Project


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"


class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/project_form.html"
    fields = ("name",)
    success_url = reverse_lazy("projects")


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "projects/project_form.html"
    fields = ("name",)
    success_url = reverse_lazy("projects")


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "projects/project_confirm_delete.html"
    success_url = reverse_lazy("projects")
