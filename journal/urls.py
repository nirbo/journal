from django.conf.urls import url
from journal import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_server/', views.add_server_form_view, name='add_server_form'),
    url(r'^show_servers/', views.show_servers, name='show_servers')
]
