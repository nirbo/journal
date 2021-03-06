from django.conf.urls import url
from journal import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^importExportCsv/$', views.upload_csv_file, name='upload_csv_file'),
    url(r'^importPhysicalServers/$', views.import_physical_servers, name='import_physical_servers'),
    url(r'^importVirtualIPs/$', views.import_virtual_ips, name='import_virtual_ips'),
    url(r'^exportPhysicalServers/$', views.export_physical_servers, name='export_physical_servers'),
    url(r'^exportVirtualIPs/$', views.export_virtual_ips, name='export_virtual_ips'),
    url(r'^deleteAllCSVs/$', views.delete_all_csvs, name='delete_all_csvs'),
    url(r'^downloadPhysicalCSVTemplate/$', views.download_physical_csv_template, name='download_physical_csv_template'),
    url(r'^downloadVirtualCSVTemplate/$', views.download_virtual_csv_template, name='download_virtual_csv_template'),
    url(r'^add_server/$', views.add_server_form_view, name='add_server_form'),
    url(r'^show_servers/', views.show_servers, name='show_servers'),
    url(r'^search/(?P<pattern>.*)$', views.search, name='search'),
    url(r'^editServer/(?P<id>\d+)$', views.edit_server_form_view, name='edit_server_form'),
    url(r'^deleteServer/(?P<id>\d+)$', views.delete_server_form_view, name='delete_server_form'),
    url(r'^manageOwners/$', views.manage_owners, name='manage_owners'),
    url(r'^deleteOwner/(?P<id>\d+)$', views.delete_owner, name='delete_owner'),
    url(r'^addOwner/$', views.add_owner, name='add_owner'),
    url(r'^editOwner/(?P<id>\d+)$', views.edit_owner, name='edit_owner'),
    url(r'^manageLocations/$', views.manage_locations, name='manage_locations'),
    url(r'^addLocation/$', views.add_location, name='add_location'),
    url(r'^deleteLocation/(?P<id>\d+)$', views.delete_location, name='delete_location'),
    url(r'^editLocation/(?P<id>\d+)$', views.edit_location, name='edit_location'),
    url(r'^manageVirtualIP/', views.manage_virtual_ip, name='manage_virtual_ips'),
    url(r'^add_virtual_ip/$', views.add_virtual_ip, name='add_virtual_ip'),
    url(r'^editVirtualIP/(?P<id>\d+)$', views.edit_virtual_ip, name='edit_virtual_ip'),
    url(r'^deleteVirtualIP/(?P<id>\d+)$', views.delete_virtual_ip, name='delete_virtual_ip'),
    url(r'^networkDetails/$', views.network_details, name='network_details'),
    url(r'^addDnsServer/$', views.add_dns_server, name='add_dns_server'),
    url(r'^editDnsServer/(?P<id>\d+)$', views.edit_dns_server, name='edit_dns_server'),
    url(r'^deleteDnsServer/(?P<id>\d+)$', views.delete_dns_server, name='delete_dns_server'),
    url(r'^addNtpServer/$', views.add_ntp_server, name='add_ntp_server'),
    url(r'^editNtpServer/(?P<id>\d+)$', views.edit_ntp_server, name='edit_ntp_server'),
    url(r'^deleteNtpServer/(?P<id>\d+)$', views.delete_ntp_server, name='delete_ntp_server'),
    url(r'^addGateway/$', views.add_gateway, name='add_gateway'),
    url(r'^editGateway/(?P<id>\d+)$', views.edit_gateway, name='edit_gateway'),
    url(r'^deleteGateway/(?P<id>\d+)$', views.delete_gateway, name='delete_gateway'),
]
