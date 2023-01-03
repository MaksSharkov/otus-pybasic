"""vault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from storage import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="projects", permanent=True)),
    path("admin/", admin.site.urls),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/create/", views.ProjectCreateView.as_view(), name="project_create"),
    path(
        "projects/update/<int:pk>/",
        views.ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "projects/delete/<int:pk>/",
        views.ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project"),
    path("secrets/create/", views.SecretCreateView.as_view(), name="secret_create"),
    path("__debug__/", include("debug_toolbar.urls")),
]
