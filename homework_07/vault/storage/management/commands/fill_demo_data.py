from django.core.management.base import BaseCommand
from storage.models import Project, Secret, Type


class Command(BaseCommand):
    help = "Fill db with demonstration data"

    def handle(self, *args, **options):
        print("Start fill db...")
        print("Remove all data")
        Project.objects.all().delete()
        Type.objects.all().delete()
        print("Add demo types")
        t_pass = Type.objects.create(name="Password")
        t_token = Type.objects.create(name="Token")
        t_other = Type.objects.create(name="Other")
        print("Add demo projects")
        p_otus = Project.objects.create(name="Otus")
        p_maks = Project.objects.create(name="Maks")
        p_anonymous = Project.objects.create(name="Anonymous")
        print("Add demo secrets")
        s_admin = Secret.objects.create(
            name="Admin", value="P@rol1", type=t_pass, project=p_otus
        )
        s_vanya = Secret.objects.create(
            name="Vanya", value="P@rol2", type=t_pass, project=p_otus, desc="Some description"
        )
        s_maks = Secret.objects.create(
            name="Maks",
            value="66ca0d2d-84e7-437e-b3f1-bccd5f6206e8",
            type=t_token,
            project=p_maks,
        )
        s_anon = Secret.objects.create(
            name="anon", value="anon", type=t_other, project=p_anonymous, desc="We are Anonymous!"
        )
        print("Fill db complete...")
