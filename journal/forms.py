from django import forms
from journal.models import Server, Location, Owner


class AddServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'


class EditServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'

    ip_field_keys = (
        'mgmt_IP',
        'data_IP_1',
        'data_IP_2',
        'bmc_IP',
    )

    def clean(self):
        cleaned_data = super(EditServerForm, self).clean()
        form_ips = self.get_form_ip_values(cleaned_data, self.ip_field_keys)
        form_server_name = self.get_form_name_value(cleaned_data)
        all_servers = Server.objects.defer('name', 'owner', 'location')

        for server in all_servers:
            current = self.get_server_ips(server, self.ip_field_keys)

            for field, ip_address in form_ips.items():
                if form_server_name != server.name:
                    if ip_address in current:
                        raise forms.ValidationError(
                            {field: ["ERROR: The IP {} is in use by another server.".format(ip_address), ]},
                            code='DuplicateIP')

    def get_form_ip_values(self, clean_data, ip_fields):
        ip_list = {}

        for field_name in ip_fields:
            ip_list[field_name] = clean_data.get(field_name)

        return ip_list

    def get_form_name_value(self, clean_data):
        return clean_data.get('name')

    def get_server_ips(self, server, ip_fields):
        server_ips = []

        for field_name in ip_fields:
            server_ips.append(getattr(server, field_name))

        return server_ips

