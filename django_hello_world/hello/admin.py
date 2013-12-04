from django.contrib import admin
from .models import Person, Request


class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)


class RequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Request, PersonAdmin)
