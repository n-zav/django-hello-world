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
    image = models.ImageField(upload_to='photos', blank=True, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Request(models.Model):
    full_path = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)


class Change(models.Model):
    TYPE_CHOICES = (
        ('created', 'create'),
        ('updated', 'update'),
        ('deleted', 'delete'),
    )
    change_type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    model_name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
