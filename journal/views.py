from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from journal.forms import AddServerForm
from journal.models import Server, Location, Owner
from journal.tables import ServerTable


# Create your views here.

def index(request):
    return render(request, 'journal/index.html')


def add_server_form_view(request):
    add_server_form = AddServerForm()

    if request.method == 'POST':
        form = AddServerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/journal')
        else:
            print("ERROR: Invalid Form")
    else:
        add_server_form = AddServerForm()

    return render(request, 'journal/add_server.html', {'add_server_form': add_server_form})


def show_servers(request):
    table = ServerTable(Server.objects.order_by('name'))
    RequestConfig(request).configure(table)

    return render(request, 'journal/show_servers.html', {'servers_table': table})
