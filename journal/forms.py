from django import forms
from journal.models import Server, Location, Owner


class AddServerForm(forms.ModelForm):
    server_name = forms.CharField(label='Server Name',
                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    server_mgmt_ip = forms.GenericIPAddressField(label='Management IP', protocol='ipv4',
                                                 widget=forms.TextInput(attrs={'class': "form-control"}))
    server_data1_ip = forms.GenericIPAddressField(label='Data Network 1', protocol='ipv4',
                                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    server_data2_ip = forms.GenericIPAddressField(label='Data Network 2', protocol='ipv4',
                                                  widget=forms.TextInput(attrs={'class': "form-control"}))
    server_owner = forms.ModelChoiceField(label='Server Owner',
                                          queryset=Owner.objects.all(),
                                          empty_label='Select Owner Name',
                                          widget=forms.Select(attrs={'class': "form-control"}))
    server_location = forms.ModelChoiceField(label='Server Location',
                                             queryset=Location.objects.all(),
                                             empty_label='Select Server Location',
                                             widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        model = Server
        fields = '__all__'
