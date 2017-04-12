from django.contrib import admin
from journal.models import Server, Location, Owner

# Register your models here.
admin.site.register(Server)
admin.site.register(Location)
admin.site.register(Owner)
