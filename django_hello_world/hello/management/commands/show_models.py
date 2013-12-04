from django.core.management.base import AppCommand


class Command(AppCommand):
    help = 'Prints model names for a given application and counts the number of objects in each model'
    args = '[appname ...]'

    def handle_app(self, app, **options):
        from django.db.models import get_models

        for model in get_models(app):
            line = "%s: %d\n" % (model._meta.object_name, model.objects.count())
            self.stdout.write(line)
            self.stderr.write("error: " + line)