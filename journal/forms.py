from django import forms
from copy import deepcopy
from journal.models import Server, Location, Owner


class AddServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'


class EditServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'

    def clean_mgmt_IP(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('mgmt_IP')

        self.validate_db_duplicates(form_field_name,
                                    form_field_ip)

        return clean_data.get('mgmt_IP')

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('data_IP_1')

        self.validate_db_duplicates(form_field_name,
                                    form_field_ip)

        return clean_data.get('data_IP_1')

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('data_IP_2')

        self.validate_db_duplicates(form_field_name,
                                    form_field_ip)

        return clean_data.get('data_IP_2')

    def clean_bmc_IP(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('bmc_IP')

        self.validate_db_duplicates(form_field_name,
                                    form_field_ip)

        return clean_data.get('bmc_IP')

    def clean(self):
        super(EditServerForm, self).clean()
        clean_data = self.cleaned_data
        has_changed = self.has_changed()
        server = Server.objects.get(name=clean_data['name'])
        cached_server = deepcopy(server)
        new_ips = set()
        old_ips = set()

        for field in self.fields:
            if '_ip' in field.lower():
                new_ips.add(str(clean_data.get(field)))
                old_ips.add(getattr(cached_server, field))

        if has_changed and len(old_ips) != len(new_ips):
            for field in self.changed_data:
                self.add_error(field, "This IP is in use by another field of this server")

    def validate_db_duplicates(self, form_server_name, field_value):
        db_servers = Server.objects.exclude(name__exact=form_server_name)
        db_values = list(db_servers.values_list())

        for record in db_values:
            if field_value in record:
                raise forms.ValidationError("The IP {} is in use by another server.".format(field_value))
