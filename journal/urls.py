from django.conf.urls import url
from journal import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_server/$', views.add_server_form_view, name='add_server_form'),
    url(r'^show_servers/', views.show_servers, name='show_servers'),
    url(r'^editServer/(?P<id>\d+)$', views.edit_server_form_view, name='edit_server_form'),
    url(r'^deleteServer/(?P<id>\d+)$', views.delete_server_form_view, name='delete_server_form'),
    url(r'^saveServer/(?P<id>\d+)$', views.save_server, name='save_server'),
]
