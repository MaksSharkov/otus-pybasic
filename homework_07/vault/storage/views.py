from django.shortcuts import render
from storage.models import Secret


# Create your views here.
def storage_get_index(request):
    secrets = Secret.objects.all()
    context = {"secrets": secrets}
    return render(
        request,
        "secrets/index.html",
        context=context,
    )
