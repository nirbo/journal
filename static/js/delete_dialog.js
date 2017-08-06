function deleteServerConfirm(id, name, searchTerm) {
    var redirect = '/journal/deleteServer/' + id + '?next=' + searchTerm;

    if (searchTerm === null) {
        redirect = '/journal/deleteServer/' + id;
    }

    $.confirm({
        theme: 'material',
        title: 'Delete Server: ' + name,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        backgroundDismiss: true,
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

function deleteOwnerConfirm(id, name) {
    var redirect = '/journal/deleteOwner/' + id;

    $.confirm({
        theme: 'material',
        title: 'Delete Owner: ' + name,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        backgroundDismiss: true,
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

function deleteLocationConfirm(id, name) {
    var redirect = '/journal/deleteLocation/' + id;

    $.confirm({
        theme: 'material',
        title: 'Delete Location: ' + name,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        backgroundDismiss: true,
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

function deleteVirtualIpConfirm(id, ipAddress, searchTerm) {
    var redirect = '/journal/deleteVirtualIP/' + id + '?next=' + searchTerm;

    if (searchTerm === null) {
        redirect = '/journal/deleteVirtualIP/' + id;
    }

    $.confirm({
        theme: 'material',
        title: 'Delete Virtual IP: ' + ipAddress,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        backgroundDismiss: true,
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

function deleteDnsConfirm(id, dnsAddress, searchTerm) {
    var redirect = '/journal/deleteDns/' + id + '?next=' + searchTerm;

    if (searchTerm === null) {
        redirect = '/journal/deleteDnsServer/' + id;
    }

    $.confirm({
        theme: 'material',
        title: 'Delete DNS: ' + dnsAddress,
        content: 'Proceed to delete?',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        escapeKey: 'cancel',
        backgroundDismiss: true,
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