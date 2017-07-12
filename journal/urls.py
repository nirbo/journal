from django.conf.urls import url
from journal import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
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
]
