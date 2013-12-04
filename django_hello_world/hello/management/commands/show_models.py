from django.core.management.base import AppCommand, CommandError


class Command(AppCommand):
    help = 'Prints model names for a given application and counts the number of objects in each model'
    args = '<app_name>'

    def handle_app(self, app_name, **options):
        from django.db.models import get_models

        try:
            for model in get_models(app_name):
                line = "%s: %d\n" % (model._meta.object_name, model.objects.count())
                self.stdout.write(line)
        except Exception as e:
            raise CommandError('An exception occurred when retrieving %s app models: %s' % (app_name, e.message))