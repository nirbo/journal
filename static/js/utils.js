function goToAddServer(url) {
    window.location.href = url
}

function goToAddOwners(url) {
    window.location.href = url
}

function goToAddLocations(url) {
    window.location.href = url
}

function goToAddVirtualIP(url) {
    window.location.href = url
}

function deleteOwnerFailed() {
    $.alert({
        theme: 'material',
        title: 'Delete Failed!',
        content: 'Unable to delete this owner while it is assigned to servers/IPs.',
        type: 'red',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            close: {
                text: 'Close',
                btnClass: 'btn',
                action: function () {}
            }
        },
    });
}

function deleteLocationFailed() {
    $.alert({
        theme: 'material',
        title: 'Delete Failed!',
        content: 'Unable to delete this location while it is assigned to servers.',
        type: 'red',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            close: {
                text: 'Close',
                btnClass: 'btn',
                action: function () {}
            }
        },
    });
}

function importPhysicalWarning() {
    var redirect = '/journal/importPhysicalServers/';

    $.confirm({
        theme: 'material',
        title: 'Import data to database',
        content: 'Are you sure you wish to import this CSV to the database?',
        type: 'red',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            confirm_import: {
                text: 'Import Data',
                btnClass: 'btn-red',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}

function importVirtualWarning() {
    var redirect = '/journal/importVirtualIPs/';

    $.confirm({
        theme: 'material',
        title: 'Import data to database',
        content: 'Are you sure you wish to import this CSV to the database?',
        type: 'red',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            confirm_import: {
                text: 'Import Data',
                btnClass: 'btn-red',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}

function clearAllCsv() {
    var redirect = '/journal/deleteAllCSVs/';

    $.confirm({
        theme: 'material',
        title: 'Delete All Uploaded CSVs',
        content: 'Are you sure you wish to delete all uploaded CSVs?',
        type: 'red',
        icon: 'glyphicon glyphicon-exclamation-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            confirm_import: {
                text: 'Delete All CSVs',
                btnClass: 'btn-red',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}

function exportPhysicalCsv() {
    var redirect = '/journal/exportPhysicalServers/';

    $.confirm({
        theme: 'material',
        title: 'Export Physical Servers',
        content: 'You are about to export the physical servers table to a CSV file',
        type: 'green',
        icon: 'glyphicon glyphicon-info-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            confirm_import: {
                text: 'Export',
                btnClass: 'btn-green',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}

function exportVirtualCsv() {
    var redirect = '/journal/exportVirtualIPs/';

    $.confirm({
        theme: 'material',
        title: 'Export Virtual IPs',
        content: 'You are about to export the virtual IPs table to a CSV file',
        type: 'green',
        icon: 'glyphicon glyphicon-info-sign',
        closeIcon: true,
        closeIconClass: 'fa fa-close',
        typeAnimated: true,
        animation: 'scaleY',
        closeAnimation: 'scaleY',
        animationBounce: 1.25,
        columnClass: 'col-md-6 col-md-offset-3',
        escapeKey: 'close',
        buttons: {
            confirm_import: {
                text: 'Export',
                btnClass: 'btn-green',
                action: function () {
                    window.location.href = redirect
                }
            },
            cancel: function () {}
        }
    });
}


window.setTimeout(function () {
    $(".alert-danger, .alert-success").fadeTo(500, 0).slideUp(500, function () {
        $(this).remove();
    });
}, 7500);