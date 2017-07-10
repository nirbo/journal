function deleteConfirm(id, name, searchTerm) {
    var redirect;

    if (searchTerm === null) {
        redirect = '/journal/deleteServer/' + id
    } else {
        redirect = '/journal/deleteServer/' + id + '?next=' + searchTerm
    }

    $.confirm({
        theme: 'material',
        title: 'Delete Server: ' + name,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        columnClass: 'col-md-6 col-md-offset-3',
        type: 'red',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        buttons: {
            confirm_delete: {
                text: 'Delete',
                btnClass: 'btn-red',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}