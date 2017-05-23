from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from journal.forms import AddServerForm, EditServerForm
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
    context = {'servers_table': table}

    return render(request, 'journal/show_servers.html', context)


def delete_server_form_view(request, id):
    server_to_delete = Server.objects.get(id=id)
    server_to_delete.delete()

    return redirect('/journal/show_servers/')


def edit_server_form_view(request, id):
    server_to_edit = Server.objects.get(id=id)
    edit_server_form = EditServerForm(instance=server_to_edit)
    context = {'edit_server_form': edit_server_form,
               'id': id}

    return render(request, 'journal/edit_server.html', context)


def save_server(request, id):
    server = Server.objects.get(id=id)

    server.name = request.POST['name']
    server.mgmt_IP = request.POST['mgmt_IP']
    server.data_IP_1 = request.POST['data_IP_1']
    server.data_IP_2 = request.POST['data_IP_2']
    server.bmc_IP = request.POST['bmc_IP']
    server.owner = Owner.objects.get(id=request.POST['owner'])
    server.location = Location.objects.get(id=request.POST['location'])

    server.save()

    return redirect('/journal/show_servers/')



