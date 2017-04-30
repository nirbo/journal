from django.shortcuts import render
from journal.forms import AddServerForm


# Create your views here.

def index(request):
    return render(request, 'journal/index.html')


def add_server_form_view(request):
    add_server_form = AddServerForm()

    if request.method == 'POST':
        form = AddServerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'journal/index.html')
        else:
            print("ERROR: Invalid Form")
    else:
        add_server_form = AddServerForm()

    return render(request, 'journal/add_server.html', {'add_server_form': add_server_form})
