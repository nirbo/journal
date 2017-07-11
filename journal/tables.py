import django_tables2 as tables
from journal.models import Server, Location, Owner


class ServerTable(tables.Table):
    class Meta:
        model = Server
        attrs = {'class': 'table table-striped table-bordered table-hover'}
        per_page = 10
        empty_text = "No servers were found."
        page_field = 'page'
        order_by_field = 'orderby'
        per_page_field = 'display'
