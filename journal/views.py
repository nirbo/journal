from django.shortcuts import render, redirect, HttpResponseRedirect
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
            return redirect('/journal/show_servers/')
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
    Server.objects.get(id=id).delete()

    return redirect('/journal/show_servers/')


def edit_server_form_view(request, id):
    server_to_edit = Server.objects.get(id=id)
    edit_server_form = EditServerForm(request.POST or None, instance=server_to_edit)
    next_page = request.GET.get('next', '')

    if request.method == 'POST':
        if edit_server_form.is_valid():
            edit_server_form.save()

            if next_page:
                return HttpResponseRedirect('/journal/search/{}'.format(next_page))

            return redirect('/journal/show_servers/')
    else:
        edit_server_form = EditServerForm(instance=server_to_edit)

    context = {'edit_server_form': edit_server_form,
               'id': id}

    return render(request, 'journal/edit_server.html', context)


def search(request, pattern):
    context = ''

    if request.method == 'POST':
        search_pattern = request.POST.get('search', '')
        table = search_lookup(request, search_pattern, pattern)

        RequestConfig(request).configure(table)
        context = {'search_results': table,
                   'search_term': search_pattern}

    elif request.method == 'GET':
        search_pattern = request.GET.get('search', '')
        table = search_lookup(request, search_pattern, pattern)

        RequestConfig(request).configure(table)
        context = {'search_results': table,
                   'search_term': search_pattern}

    return render(request, 'journal/search.html', context)


def search_lookup(request, search_pattern, pattern):
    servers = Server.objects.all()
    owners = Owner.objects.all()
    locations = Location.objects.all()
    table_data = set()
    table = ''

    if pattern:
        search_pattern = pattern

    for server in servers.values():
        server_values = []

        for key, value in server.items():
            if 'owner' in key:
                server_values.append(list(owners.filter(id=value))[-1].owner_name)
            elif 'location' in key:
                server_values.append(list(locations.filter(id=value))[-1].physical_location)
            else:
                server_values.append(value)

        for value in server_values:
            if search_pattern.lower() in str(value).lower():
                table_data.add(server_values[0])

        table = ServerTable(servers.filter(id__in=list(table_data)).order_by('name'))

    return table
