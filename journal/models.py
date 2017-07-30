from django.db import models
import os.path


class Server(models.Model):
    name = models.CharField(max_length=64, unique=True)
    mgmt_IP = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='both', default='')
    data_IP_1 = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='both', default='')
    data_IP_2 = models.GenericIPAddressField(blank=True, unique=True, null=True, protocol='both')
    bmc_IP = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='both', default='')
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


class VirtualIP(models.Model):
    ip_address = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='both', default='')
    netmask = models.GenericIPAddressField(blank=False, unique=False, null=False, protocol='both', default='')
    vlan = models.CharField(max_length=64, blank=True, unique=False, null=True)
    data_IP_1 = models.GenericIPAddressField(blank=False, unique=True, null=False, protocol='both', default='')
    data_IP_2 = models.GenericIPAddressField(blank=True, unique=True, null=True, protocol='both')
    owner = models.ForeignKey('Owner')
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.ip_address


class CSVUpload(models.Model):
    file = models.FileField(max_length=255, upload_to='csv/import/')

    def __unicode__(self):
        return self.file

    def filename(self):
        return os.path.basename(self.file.name)

