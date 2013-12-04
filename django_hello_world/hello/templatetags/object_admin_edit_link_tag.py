from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def admin_edit_link(input_object):
    return reverse('admin:%s_%s_change' % (input_object._meta.app_label, input_object._meta.module_name),
                   args=[input_object.pk])
