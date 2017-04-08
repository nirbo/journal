from django.db import models


# Create your models here.

class Server(models.Model):
    server_name = models.CharField(max_length=64, unique=True)
    server_mgmt_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    server_data1_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    server_data2_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')
    server_owner = models.CharField(max_length=64, unique=False)
    server_location = models.ForeignKey('Location')

    def __str__(self):
        return self.server_name


class Location(models.Model):
    physical_location = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.physical_location
