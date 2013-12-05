from StringIO import StringIO
from django.test import TestCase
from django.core.management import call_command


class ShowModelsTestCase(TestCase):

    def test_data_in_stdout(self):
        stdout = StringIO()
        stderr = StringIO()
        call_command('show_models', 'hello', stdout=stdout, stderr=stderr, verbosity=0, interactive=False)
        stdout.seek(0)
        self.assertIn('Person: 1', stdout.read())
        stderr.seek(0)
        self.assertIn('error:', stderr.read())
