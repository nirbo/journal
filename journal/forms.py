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

    def clean_name(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        instance = self.instance
        db_values = self.query_db_exclude_name(instance.name)

        for record in db_values:
            if form_field_name in record.values():
                raise forms.ValidationError("The name '{}' is already in use by another server".format(form_field_name))

        return form_field_name

    def clean_mgmt_IP(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('mgmt_IP')
        name_has_errors = self.has_error('name')

        if not name_has_errors:
            self.validate_db_duplicates(form_field_name,
                                        form_field_ip)
        return form_field_ip

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('data_IP_1')
        name_has_errors = self.has_error('name')

        if not name_has_errors:
            self.validate_db_duplicates(form_field_name,
                                        form_field_ip)
        return form_field_ip

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('data_IP_2')
        name_has_errors = self.has_error('name')

        if not name_has_errors:
            self.validate_db_duplicates(form_field_name,
                                        form_field_ip)
        return form_field_ip

    def clean_bmc_IP(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data.get('name')
        form_field_ip = clean_data.get('bmc_IP')
        name_has_errors = self.has_error('name')

        if not name_has_errors:
            self.validate_db_duplicates(form_field_name,
                                        form_field_ip)
        return form_field_ip

    def clean(self):
        super(EditServerForm, self).clean()
        clean_data = self.cleaned_data
        has_changed = self.has_changed()
        instance = self.instance
        new_ips = set()
        old_ips = set()

        for field in self.fields:
            if '_ip' in field.lower():
                new_ips.add(str(clean_data.get(field)))
                old_ips.add(getattr(instance, field))

        if has_changed and len(old_ips) != len(new_ips):
            for field in self.changed_data:
                if '_ip' in field.lower():
                    self.add_error(field, "The IP address is already in use by another field of this server")

    def validate_db_duplicates(self, form_server_name, field_value):
        db_values = ''

        if self.has_changed():
            if 'name' in self.changed_data:
                db_values = self.query_db_name_change(self.instance)
            else:
                db_values = self.query_db_exclude_name(form_server_name)

        for record in db_values:
            if field_value in record.values():
                raise forms.ValidationError("The IP address '{}' is already in use by another server.".format(field_value))

    def query_db_exclude_name(self, excluded_name):
        return Server.objects.exclude(name__exact=excluded_name).values()

    def query_db_name_change(self, instance):
        old_name = instance.name
        new_name = self.cleaned_data['name']

        return Server.objects.exclude(name__in=(old_name, new_name)).values()
