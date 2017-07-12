import django_tables2 as tables
from journal.models import Server, Location, Owner


class ServerTable(tables.Table):
    class Meta:
        model = Server
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        per_page = 10
        empty_text = "No servers found."
        page_field = 'page'
        order_by_field = 'orderby'
        per_page_field = 'display'


class OwnerTable(tables.Table):
    class Meta:
        model = Owner
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        template = 'journal/owner_table_template.html'
        per_page = 10
        empty_text = "No owners found."
        prefix = 'owner'
        page_field = 'page'
        per_page_field = 'display'


class LocationTable(tables.Table):
    class Meta:
        model = Location
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        template = 'journal/location_table_template.html'
        per_page = 10
        empty_text = 'No locations found.'
        prefix = 'location'
        page_field = 'page'
        per_page_field = 'display'
