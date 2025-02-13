// STAFF DASHBOARD SCRIPT //

// Showing modal if there is an add, update or delete request.
window.onload = () => {
    const dashboardModalElement = document.getElementById('dashboard-modal');
    if (dashboardModalElement) {
        const dashboardModal = new bootstrap.Modal(dashboardModalElement);
        dashboardModal.show();
    }
};

// Display chosen image filename when selecting image for product
$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`${file.name}`);
});

// Display new image next to current image when updating product
const imageInput = document.querySelector('input[name="image"]');
const previewImage = document.getElementById('previewImage');
const newImagePreview = document.getElementById('new-image-preview')

if (imageInput) {
    imageInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                newImagePreview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });
}

// Show new topic field in FAQ form if new topic is selected
const idTopic = document.getElementById('id_topic')

if (idTopic) {
    idTopic.addEventListener('change', function() {
        let newTopicField = document.getElementById('new-topic-field');
        if (this.value === 'new') {
            newTopicField.style.display = 'block';
        } else {
            newTopicField.style.display = 'none';
            document.getElementById('id_new_topic').value = '';
        }
    });
}

// DASHBOARD BUTTON SPINNERS //
const spinnerButtons = document.getElementsByClassName('btn-with-spinner');
const dashboardModalConfirmButton = document.getElementById('dashboard-modal-confirm');

// Activating spinner on anchor elements.
Array.from(spinnerButtons).forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        
        const buttonElement = this;
        
        buttonElement.querySelector('.btn-text').classList.add('d-none');
        buttonElement.querySelector('.spinner-border').classList.remove('d-none');
        
        setTimeout(() => {
            window.location.href = buttonElement.href;
        }, 1);
    });
});

// Activating spinner on button elements.
if (dashboardModalConfirmButton) {
    dashboardModalConfirmButton.addEventListener('click', function() {
        const buttonElement = this;
        
        buttonElement.querySelector('.btn-text').classList.add('d-none');
        buttonElement.querySelector('.spinner-border').classList.remove('d-none');
    })
}