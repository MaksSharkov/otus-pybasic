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
from .forms import ProjectModelForm, SecretModelForm


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
    form_class = ProjectModelForm
    success_url = reverse_lazy("projects")


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "projects/project_form.html"
    form_class = ProjectModelForm
    success_url = reverse_lazy("projects")


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "projects/project_confirm_delete.html"
    success_url = reverse_lazy("projects")


class SecretCreateView(CreateView):
    model = Secret
    template_name = "secrets/secret_form.html"
    form_class = SecretModelForm

    def post(self, request, *args, **kwargs):
        self.project_pk = kwargs["project_pk"]
        return super().post(self, request, *args, **kwargs)

    def form_valid(self, form):
        project = Project.objects.get(id=self.project_pk)
        form.instance.project = project
        self.success_url = reverse_lazy("project", args=[self.project_pk])
        return super().form_valid(form)


class SecretDeleteView(DeleteView):
    model = Secret
    template_name = "secrets/secret_confirm_delete.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy("project", args=[kwargs["project_pk"]])
        return super().post(self, request, *args, **kwargs)


class SecretUpdateView(UpdateView):
    model = Secret
    template_name = "secrets/secret_form.html"
    form_class = SecretModelForm

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy("project", args=[kwargs["project_pk"]])
        return super().post(self, request, *args, **kwargs)
