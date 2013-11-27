from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    biography = models.TextField()
    email = models.EmailField(unique=True)
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=32)
    other_contacts = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Request(models.Model):
    full_path = models.TextField()
