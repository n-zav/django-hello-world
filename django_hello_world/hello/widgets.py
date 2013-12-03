from django.conf import settings
from django.forms.widgets import Input
from django.utils.safestring import mark_safe


class DatePickerInput(Input):
    class Media:
        css = {
            'all': (settings.STATIC_URL + 'css/jquery-ui.css',),
        }
        js = (settings.STATIC_URL + 'js/jquery.min.js',
              settings.STATIC_URL + 'js/jquery-ui.min.js'
        )

    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        if 'class' in attrs:
            attrs['class'] += ' datepicker'
        else:
            attrs['class'] = 'datepicker'

        rendered = super(DatePickerInput, self).render(name, value, attrs)

        return rendered + mark_safe(u'''
        <script type="text/javascript">
            $(function() {
                $('.datepicker').datepicker();
            });
        </script>
        ''')
