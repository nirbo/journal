import django_tables2 as tables
from journal.models import Server, Location, Owner


class ServerTable(tables.Table):
    class Meta:
        model = Server
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        per_page = 25
