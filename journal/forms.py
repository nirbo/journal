from django import forms
from django.db.models import Q
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
        self.validate_duplicates(clean_data.get('name'),
                                 clean_data.get('mgmt_IP'))

        return clean_data.get('mgmt_IP')

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        self.validate_duplicates(clean_data.get('name'),
                                 clean_data.get('data_IP_1'))

        return clean_data.get('data_IP_1')

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        self.validate_duplicates(clean_data.get('name'),
                                 clean_data.get('data_IP_2'))

        return clean_data.get('data_IP_2')

    def clean_bmc_IP(self):
        clean_data = self.cleaned_data
        self.validate_duplicates(clean_data.get('name'),
                                 clean_data.get('bmc_IP'))

        return clean_data.get('bmc_IP')

    def validate_duplicates(self, form_server_name, field_value):
        db_servers = Server.objects.exclude(name__exact=form_server_name)

        db_values = list(db_servers.values_list())
        for record in db_values:
            if field_value in record:
                print("{} Found".format(field_value))
                raise forms.ValidationError("The IP {} is in use by another server.".format(field_value))
