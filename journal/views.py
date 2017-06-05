from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from journal.forms import AddServerForm, EditServerForm
from journal.models import Server, Location, Owner
from journal.tables import ServerTable


def index(request):
    return render(request, 'journal/index.html')


def add_server_form_view(request):
    if request.method == 'POST':
        add_server_form = AddServerForm(request.POST)

        if add_server_form.is_valid():
            add_server_form.save(commit=True)
            return redirect('/journal')
        else:
            print(add_server_form.errors)
    else:
        add_server_form = AddServerForm()

    context = {'add_server_form': add_server_form}

    return render(request, 'journal/add_server.html', context)


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
    edit_server_form = EditServerForm(request.POST or None, instance=server_to_edit)

    if request.method == 'POST':
        if edit_server_form.is_valid():
            edit_server_form.save()
            return redirect('/journal/show_servers/')
    else:
        edit_server_form = EditServerForm(instance=server_to_edit)

    context = {'edit_server_form': edit_server_form,
               'id': id}

    return render(request, 'journal/edit_server.html', context)
