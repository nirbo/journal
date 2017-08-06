from django.contrib import admin
from journal.models import Server, Location, Owner, VirtualIP, CSVUpload, DNS, NTP
from import_export import resources

# Register your models here.
admin.site.register(Server)
admin.site.register(Location)
admin.site.register(Owner)
admin.site.register(VirtualIP)
admin.site.register(CSVUpload)
admin.site.register(DNS)
admin.site.register(NTP)


class ServerResource(resources.ModelResource):
    class Meta:
        model = Server


class VirtualIPResource(resources.ModelResource):
    class Meta:
        model = VirtualIP
