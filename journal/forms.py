from django import forms
from django.core import validators
from journal.models import Server, Location


class AddServerForm(forms.ModelForm):
    server_name = forms.CharField(label='Server Name')
    server_mgmt_ip = forms.GenericIPAddressField(label='MGMT IP', protocol='ipv4')
    server_data1_ip = forms.GenericIPAddressField(label='Data Network 1', protocol='ipv4')
    server_data2_ip = forms.GenericIPAddressField(label='Data Network 2', protocol='ipv4')
    server_owner = forms.CharField(label='Server Owner')
    server_location = forms.ModelChoiceField(label='Server Location',
                                             queryset=Location.objects.all(),
                                             empty_label='Select Server Location')

    class Meta:
        model = Server
        fields = '__all__'
