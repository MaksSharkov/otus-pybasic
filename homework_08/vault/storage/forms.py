from django import forms
from .models import Project, Secret, Type


class ProjectModelForm(forms.ModelForm):
    name = forms.CharField(
        label="Название", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Project
        fields = ("name",)


class SecretModelForm(forms.ModelForm):
    name = forms.CharField(
        label="Название", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    value = forms.CharField(
        label="Значение",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
    )
    desc = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        required=False,
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        label="Проект",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        label="Тип",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Secret
        fields = (
            "name",
            "value",
            "desc",
            "project",
            "type",
        )
