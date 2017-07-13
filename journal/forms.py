from django import forms
from journal.models import Server, Location, Owner, VirtualIP


class AddServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data['name']

        if self.does_record_exist(form_field_name):
            raise forms.ValidationError("The name '{}' is already in use by another server".format(form_field_name))

        return form_field_name

    def clean_mgmt_IP(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['mgmt_IP']

        if self.does_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['data_IP_1']

        if self.does_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['data_IP_2']

        if self.does_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_bmc_IP(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['bmc_IP']

        if self.does_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def does_record_exist(self, check_value):
        db_values = self.query_entire_db()

        for record in db_values:
            if check_value in record.values():
                return True

        return False

    def query_entire_db(self):
        return list(Server.objects.all().values())


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
        super(EditOwnerForm, self).clean()
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
                raise forms.ValidationError("The IP address '{}' is already in use by another server".format(field_value))

    def query_db_exclude_name(self, excluded_name):
        return Server.objects.exclude(name__exact=excluded_name).values()

    def query_db_name_change(self, instance):
        old_name = instance.name
        new_name = self.cleaned_data['name']

        return Server.objects.exclude(name__in=(old_name, new_name)).values()


class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class EditOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class EditLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class AddVirtualIpForm(forms.ModelForm):
    class Meta:
        model = VirtualIP
        fields = '__all__'


class EditVirtualIpForm(forms.ModelForm):
    class Meta:
        model = VirtualIP
        fields = '__all__'
