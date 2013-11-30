MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) test hello

run:
	python django_hello_world/manage.py runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) migrate hello

loaddata:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) loaddata initial_data.json
