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
