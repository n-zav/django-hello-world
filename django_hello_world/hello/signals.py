from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_hello_world.hello.models import Change


@receiver(post_save)
def object_update(sender, **kwargs):
    model_name = sender._meta.object_name
    if model_name == 'Change':
        pass
    else:
        change_type = 'created' if kwargs.get('created', True) else 'updated'
        c = Change(change_type=change_type, model_name=model_name)
        c.save()


@receiver(post_delete)
def object_delete(sender, **kwargs):
    model_name = sender._meta.object_name
    if model_name == 'Change':
        pass
    else:
        change_type = 'deleted'
        c = Change(change_type=change_type, model_name=model_name)
        c.save()
