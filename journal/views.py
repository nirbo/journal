from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.utils.encoding import smart_str
from django_tables2 import RequestConfig
from import_export import resources
from journal.admin import ServerResource, VirtualIPResource
from journal.forms import AddServerForm, EditServerForm, EditOwnerForm, AddOwnerForm, AddLocationForm, \
    EditLocationForm, AddVirtualIpForm, EditVirtualIpForm, CSVFileForm
from journal.models import Server, Location, Owner, VirtualIP, CSVUpload
from journal.tables import ServerTable, OwnerTable, LocationTable, VirtualIpTable
import os.path
import shutil
import tablib


def index(request):
    return render(request, 'journal/index.html')


def settings(request):
    return render(request, 'journal/settings.html')


def upload_csv_file(request):
    if request.method == 'POST':
        files_db = CSVUpload.objects.all()
        form = CSVFileForm(request.POST, request.FILES)
        import_path = 'media/csv/import/'
        import_file = ''

        if form.is_valid():
            if request.POST.get('physical-servers-submit'):
                import_file = 'physical_servers_import.csv'
            elif request.POST.get('virtual-ips-submit'):
                import_file = 'virtual_ips_import.csv'

            full_path_import_file = os.path.join(import_path, import_file)
            new_file = CSVUpload(file=request.FILES['file'])

            if new_file.filename().lower().endswith('.csv'):
                new_file.save()
                messages.success(request, 'CSV file uploaded')
            else:
                messages.error(request, 'Wrong file type uploaded; please try again with a CSV file')
                return HttpResponseRedirect('/journal/importExportCsv/')

            if len(os.listdir(import_path)) == 1:
                for file in os.listdir(import_path):
                    file_location = os.path.join(import_path + file)
                    os.rename(file_location, full_path_import_file)
            else:
                shutil.rmtree(import_path)
                os.makedirs(import_path)
                files_db.delete()

            return HttpResponseRedirect('/journal/importExportCsv/')
    else:
        form = CSVFileForm()

    files_db = CSVUpload.objects.all()
    context = {'files': files_db,
               'form': form}

    return render(request, 'journal/import_export_csv.html', context)


def import_physical_servers(request):
    import_path = 'media/csv/import/'
    import_file = 'physical_servers_import.csv'
    full_path_import_file = os.path.join(import_path, import_file)
    files_db = CSVUpload.objects.all()
    server_resource = resources.modelresource_factory(model=Server)()

    try:
        dataset = tablib.Dataset().load(open(full_path_import_file).read())
        test = server_resource.import_data(dataset, dry_run=True)

        if not test.has_errors():
            result = server_resource.import_data(dataset, dry_run=False)
            if result:
                files_db.delete()
                os.unlink(full_path_import_file)
                messages.success(request, "Data imported successfully")
        else:
            files_db.delete()
            os.unlink(full_path_import_file)
            messages.error(request, "Failed to import data, possible duplicate entry or incorrect CSV content syntax")

    except FileNotFoundError:
        messages.error(request, "No CSV file found; Please upload one and try again")

    return HttpResponseRedirect('/journal/importExportCsv/')


def import_virtual_ips(request):
    import_path = 'media/csv/import/'
    import_file = 'virtual_ips_import.csv'
    full_path_import_file = os.path.join(import_path, import_file)
    files_db = CSVUpload.objects.all()
    virtual_ip_resource = resources.modelresource_factory(model=VirtualIP)()

    try:
        dataset = tablib.Dataset().load(open(full_path_import_file).read())
        test = virtual_ip_resource.import_data(dataset, dry_run=True)

        if not test.has_errors():
            result = virtual_ip_resource.import_data(dataset, dry_run=False)
            if result:
                files_db.delete()
                os.unlink(full_path_import_file)
                messages.success(request, "Data imported successfully")
        else:
            files_db.delete()
            os.unlink(full_path_import_file)
            messages.error(request, "Failed to import data, possible duplicate entry or incorrect CSV content syntax")

    except FileNotFoundError:
        messages.error(request, "No CSV file found; Please upload one and try again")

    return HttpResponseRedirect('/journal/importExportCsv/')


def export_physical_servers(request):
    export_file = 'media/csv/export/physical_servers_export.csv'

    if os.path.isfile(export_file):
        os.remove(export_file)

    try:
        with open(export_file, 'w') as exported_csv:
            exported_csv.write("id,name,mgmt_IP,data_IP_1,data_IP_2,bmc_IP,owner,location\n")
            for row in ServerResource().export():
                for column in row:
                    exported_csv.write("{},".format(column))
                exported_csv.write('\n')
            exported_csv.close()

        response = HttpResponse(open(export_file, 'rb'), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(os.path.basename(export_file)))
        response['X-Sendfile'] = smart_str(export_file)

        return response

    except Exception:
        messages.error(request, 'Failed to export physical servers CSV file')

    return HttpResponseRedirect('/journal/importExportCsv/')


def export_virtual_ips(request):
    export_file = 'media/csv/export/virtual_ips_export.csv'

    if os.path.isfile(export_file):
        os.remove(export_file)

    try:
        with open(export_file, 'w') as exported_csv:
            exported_csv.write("id,ip_address,netmask,vlan,data_IP_1,data_IP_2,owner,location\n")
            for row in VirtualIPResource().export():
                for column in row:
                    exported_csv.write("{},".format(column))
                exported_csv.write('\n')
            exported_csv.close()

        response = HttpResponse(open(export_file, 'rb'), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(os.path.basename(export_file)))
        response['X-Sendfile'] = smart_str(export_file)

        return response

    except Exception:
        messages.error(request, 'Failed to export virtual IPs CSV file')

    return HttpResponseRedirect('/journal/importExportCsv/')


def delete_all_csvs(request):
    import_path = 'media/csv/import/'

    try:
        shutil.rmtree(import_path)
        os.makedirs(import_path)
        CSVUpload.objects.all().delete()
        messages.success(request, 'All CSVs deleted successfully')
    except Exception:
        messages.error(request, 'Failed to delete all CSVs')

    return HttpResponseRedirect('/journal/importExportCsv/')

def import_export_csv(request):
    return render(request, 'journal/import_export_csv.html')


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
    next_page = request.GET.get('next', '')

    if next_page:
        return HttpResponseRedirect('/journal/search/{}'.format(next_page))

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
    # context = ''
    search_pattern = ''

    if request.method == 'POST':
        search_pattern = request.POST.get('search', '')
    elif request.method == 'GET':
        search_pattern = request.GET.get('search', '')

    physical_server_table = physical_search_lookup(request, search_pattern, pattern)
    virtual_ips_table = virtual_search_lookup(request, search_pattern, pattern)

    RequestConfig(request).configure(physical_server_table)
    RequestConfig(request).configure(virtual_ips_table)
    context = {'physical_search_results': physical_server_table,
               'virtual_search_results': virtual_ips_table,
               'search_term': search_pattern}

    return render(request, 'journal/search.html', context)


def physical_search_lookup(request, search_pattern, pattern):
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


def virtual_search_lookup(request, search_pattern, pattern):
    virtual_ips = VirtualIP.objects.all()
    owners = Owner.objects.all()
    locations = Location.objects.all()
    table_data = set()
    table = ''

    if pattern:
        search_pattern = pattern

    for virtual_ip in virtual_ips.values():
        virtual_ip_values = []

        for key, value in virtual_ip.items():
            if 'owner' in key:
                virtual_ip_values.append(list(owners.filter(id=value))[-1].owner_name)
            elif 'location' in key:
                virtual_ip_values.append(list(locations.filter(id=value))[-1].physical_location)
            else:
                virtual_ip_values.append(value)

        for value in virtual_ip_values:
            if search_pattern.lower() in str(value).lower():
                table_data.add(virtual_ip_values[0])

        table = VirtualIpTable(virtual_ips.filter(id__in=list(table_data)).order_by('ip_address'))

    return table


def manage_owners(request):
    table = OwnerTable(Owner.objects.order_by('owner_name'))
    RequestConfig(request).configure(table)
    context = {'owners_table': table}

    return render(request, 'journal/manage_owners.html', context)


def delete_owner(request, id):
    if is_safe_to_delete_owner(id):
        Owner.objects.get(id=id).delete()
    else:
        messages.error(request, 'Failed to Delete Owner')

    return redirect('/journal/manageOwners/')


def is_safe_to_delete_owner(id):
    owner_servers = Server.objects.filter(owner__in=id).count()

    if owner_servers == 0:
        return True

    return False


def add_owner(request):
    if request.method == 'POST':
        add_owner_form = AddOwnerForm(request.POST)

        if add_owner_form.is_valid():
            add_owner_form.save(commit=True)
            return redirect('/journal/manageOwners/')
    else:
        add_owner_form = AddOwnerForm()

    context = {'add_owner_form': add_owner_form}

    return render(request, 'journal/add_owner.html', context)


def edit_owner(request, id):
    owner_to_edit = Owner.objects.get(id=id)
    edit_owner_form = EditOwnerForm(request.POST or None, instance=owner_to_edit)

    if request.method == 'POST':
        if edit_owner_form.is_valid():
            edit_owner_form.save()

            return redirect('/journal/manageOwners/')
    else:
        edit_owner_form = EditOwnerForm(instance=owner_to_edit)

    context = {'edit_owner_form': edit_owner_form,
               'id': id}

    return render(request, 'journal/edit_owner.html', context)


def manage_locations(request):
    table = LocationTable(Location.objects.order_by('physical_location'))
    RequestConfig(request).configure(table)
    context = {'locations_table': table}

    return render(request, 'journal/manage_locations.html', context)


def add_location(request):
    if request.method == 'POST':
        add_location_form = AddLocationForm(request.POST)

        if add_location_form.is_valid():
            add_location_form.save(commit=True)
            return redirect('/journal/manageLocations/')
    else:
        add_location_form = AddLocationForm()

    context = {'add_location_form': add_location_form}

    return render(request, 'journal/add_location.html', context)


def delete_location(request, id):
    if is_safe_to_delete_location(id):
        Location.objects.get(id=id).delete()
    else:
        messages.error(request, 'Failed to Delete Location')

    return redirect('/journal/manageLocations/')


def is_safe_to_delete_location(id):
    owner_servers = Server.objects.filter(location__in=id).count()

    if owner_servers == 0:
        return True

    return False


def edit_location(request, id):
    location_to_edit = Location.objects.get(id=id)
    edit_location_form = EditLocationForm(request.POST or None, instance=location_to_edit)

    if request.method == 'POST':
        if edit_location_form.is_valid():
            edit_location_form.save()

            return redirect('/journal/manageLocations/')
    else:
        edit_location_form = EditLocationForm(instance=location_to_edit)

    context = {'edit_location_form': edit_location_form,
               'id': id}

    return render(request, 'journal/edit_location.html', context)


def manage_virtual_ip(request):
    table = VirtualIpTable(VirtualIP.objects.order_by('ip_address'))
    RequestConfig(request).configure(table)
    context = {'virtual_ip_table': table}

    return render(request, 'journal/manage_virtual_ip.html', context)


def add_virtual_ip(request):
    if request.method == 'POST':
        add_virtual_ip_form = AddVirtualIpForm(request.POST)

        if add_virtual_ip_form.is_valid():
            add_virtual_ip_form.save(commit=True)
            return redirect('/journal/manageVirtualIP/')
    else:
        add_virtual_ip_form = AddVirtualIpForm()

    context = {'add_virtual_ip_form': add_virtual_ip_form}

    return render(request, 'journal/add_virtual_ip.html', context)


def edit_virtual_ip(request, id):
    virtual_ip_to_edit = VirtualIP.objects.get(id=id)
    edit_virtual_ip_form = EditVirtualIpForm(request.POST or None, instance=virtual_ip_to_edit)
    next_page = request.GET.get('next', '')

    if request.method == 'POST':
        if edit_virtual_ip_form.is_valid():
            edit_virtual_ip_form.save()

            if next_page:
                return HttpResponseRedirect('/journal/search/{}'.format(next_page))

            return redirect('/journal/manageVirtualIP/')
    else:
        edit_virtual_ip_form = EditVirtualIpForm(instance=virtual_ip_to_edit)

    context = {'edit_virtual_ip_form': edit_virtual_ip_form,
               'id': id}

    return render(request, 'journal/edit_virtual_ip.html', context)


def delete_virtual_ip(request, id):
    VirtualIP.objects.get(id=id).delete()
    next_page = request.GET.get('next', '')

    if next_page:
        return HttpResponseRedirect('/journal/search/{}'.format(next_page))

    return redirect('/journal/manageVirtualIP/')
