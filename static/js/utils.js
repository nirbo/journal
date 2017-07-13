function goToAddServer(url) {
    window.location.href = url
}

function goToAddOwners(url) {
    window.location.href = url
}

function goToAddLocations(url) {
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
