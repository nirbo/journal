import django_tables2 as tables
from journal.models import Server, Location, Owner


class ServerTable(tables.Table):
    class Meta:
        model = Server
        attrs = {'class': 'servers_table table table-striped table-bordered table-hover'}
        fields = ('name', 'mgmt_IP', 'data_IP_1', 'data_IP_2', 'bmc_IP', 'owner', 'location')
