window.onload = () => {
    const settingsModalElement = document.getElementById('settings-modal');
    if (settingsModalElement) {
        const settingsModal = new bootstrap.Modal(settingsModalElement);
        settingsModal.show();
    }
};

$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});