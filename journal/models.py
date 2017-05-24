from django.db import models


# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=64, unique=True)
    mgmt_IP = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='IPv4')
    data_IP_1 = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='IPv4')
    data_IP_2 = models.GenericIPAddressField(blank=True, unique=True, null=True, protocol='IPv4')
    bmc_IP = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='IPv4')
    owner = models.ForeignKey('Owner')
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.name


class Location(models.Model):
    physical_location = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.physical_location


class Owner(models.Model):
    owner_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.owner_name
