from django import forms
from journal.models import Server, Location, Owner, VirtualIP, DNS, NTP, Gateway


class CSVFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV file')


class AddServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data
        form_field_name = clean_data['name']

        if self.does_server_record_exist(form_field_name):
            raise forms.ValidationError("The name '{}' is already in use by another server".format(form_field_name))

        return form_field_name

    def clean_mgmt_IP(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['mgmt_IP']

        if self.does_server_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['data_IP_1']

        if self.does_server_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['data_IP_2']

        if self.does_server_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def clean_bmc_IP(self):
        clean_data = self.cleaned_data
        form_field_ip = clean_data['bmc_IP']

        if self.does_server_record_exist(form_field_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another server".format(form_field_ip))

        return form_field_ip

    def does_server_record_exist(self, check_value):
        db_values = self.query_server_entire_db()

        for record in db_values:
            if check_value in record.values():
                return True

        return False

    def query_server_entire_db(self):
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

    def clean_ip_address(self):
        clean_data = self.cleaned_data
        form_ip_address = clean_data['ip_address']

        if self.does_virtual_ip_record_exist(form_ip_address):
            raise forms.ValidationError("The IP address '{}' is already in use by another record".format(form_ip_address))

        return form_ip_address

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_data_ip = clean_data['data_IP_1']

        if self.does_virtual_ip_record_exist(form_field_data_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another record".format(form_field_data_ip))

        return form_field_data_ip

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_data_ip = clean_data['data_IP_2']

        if self.does_virtual_ip_record_exist(form_field_data_ip):
            raise forms.ValidationError("The IP address '{}' is already in use by another record"
                                        .format(form_field_data_ip))

        return form_field_data_ip

    def does_virtual_ip_record_exist(self, check_value):
        db_values = self.query_virtual_ip_entire_db()

        for record in db_values:
            if check_value in record.values():
                return True

        return False

    def query_virtual_ip_entire_db(self):
        return list(VirtualIP.objects.all().values())


class EditVirtualIpForm(forms.ModelForm):
    class Meta:
        model = VirtualIP
        fields = '__all__'

    def clean_ip_address(self):
        clean_data = self.cleaned_data
        form_field_ip_address = clean_data.get('ip_address')
        ip_address_has_errors = self.has_error('ip_address')

        if not ip_address_has_errors:
            self.validate_db_duplicates(form_field_ip_address, self.instance.ip_address)

        return form_field_ip_address

    def clean_data_IP_1(self):
        clean_data = self.cleaned_data
        form_field_ip_address = clean_data.get('ip_address')
        form_field_data_ip = clean_data.get('data_IP_1')
        ip_address_has_errors = self.has_error('ip_address')

        if not ip_address_has_errors:
            self.validate_db_duplicates(form_field_ip_address,
                                        form_field_data_ip)
        return form_field_data_ip

    def clean_data_IP_2(self):
        clean_data = self.cleaned_data
        form_field_ip_address = clean_data.get('ip_address')
        form_field_data_ip = clean_data.get('data_IP_2')
        ip_address_has_errors = self.has_error('ip_address')

        if not ip_address_has_errors:
            self.validate_db_duplicates(form_field_ip_address,
                                        form_field_data_ip)
        return form_field_data_ip

    def clean(self):
        super(EditVirtualIpForm, self).clean()
        clean_data = self.cleaned_data
        has_changed = self.has_changed()
        instance = self.instance
        new_ips = set()
        old_ips = set()

        for field in self.fields:
            if '_ip' in field:
                new_ips.add(str(clean_data.get(field)))
                old_ips.add(getattr(instance, field))

        if has_changed and len(old_ips) != len(new_ips):
            for field in self.changed_data:
                if '_ip' in field:
                    self.add_error(field, "The IP address is already in use by another field of this record")

    def validate_db_duplicates(self, form_virtual_ip_address, field_value=''):
        db_values = ''

        if self.has_changed():
            if 'ip_address' in self.changed_data:
                db_values = self.query_db_ip_address_change(self.instance)
            else:
                db_values = self.query_db_exclude_ip_address(form_virtual_ip_address)

        for record in db_values:
            if field_value in record.values():
                raise forms.ValidationError("The IP address '{}' is already in use by another record"
                                            .format(field_value))

        self.check_self_ip_duplicate()

    def query_db_exclude_ip_address(self, excluded_ip_address):
        return VirtualIP.objects.exclude(ip_address__exact=excluded_ip_address).values()

    def query_db_ip_address_change(self, instance):
        old_ip_address = instance.ip_address
        new_ip_address = self.cleaned_data['ip_address']

        return VirtualIP.objects.exclude(ip_address__in=(old_ip_address, new_ip_address)).values()

    def check_self_ip_duplicate(self):
        cleaned_data = self.cleaned_data
        instance = self.instance
        error_field = ''

        for field in self.cleaned_data:
            if '_ip' in field.lower():
                if instance.ip_address == cleaned_data.get(field):
                    error_field = field

        if error_field:
            raise forms.ValidationError("The IP address is already in use by another field of this record", error_field)


class AddDNSForm(forms.ModelForm):
    class Meta:
        model = DNS
        fields = '__all__'


class EditDNSForm(forms.ModelForm):
    class Meta:
        model = DNS
        fields = '__all__'


class AddNTPForm(forms.ModelForm):
    class Meta:
        model = NTP
        fields = '__all__'


class EditNTPForm(forms.ModelForm):
    class Meta:
        model = NTP
        fields = '__all__'


class AddGatewayForm(forms.ModelForm):
    class Meta:
        model = Gateway
        fields = '__all__'


class EditGatewayForm(forms.ModelForm):
    class Meta:
        model = Gateway
        fields = '__all__'
