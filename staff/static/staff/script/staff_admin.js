window.onload = () => {
    const dashboardModalElement = document.getElementById('dashboard-modal');
    if (dashboardModalElement) {
        const dashboardModal = new bootstrap.Modal(dashboardModalElement);
        dashboardModal.show();
    }
};

$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`${file.name}`);
});

const imageInput = document.querySelector('input[name="image"]');
const previewImage = document.getElementById('previewImage');
const newImagePreview = document.getElementById('new-image-preview')

if (imageInput) {
    imageInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                newImagePreview.style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    });
}

const idTopic = document.getElementById("id_topic")

idTopic.addEventListener("change", function() {
    let newTopicField = document.getElementById("new-topic-field");
    if (this.value === "new") {
        newTopicField.style.display = "block";
    } else {
        newTopicField.style.display = "none";
        document.getElementById("id_new_topic").value = ""; // Clear new topic field if hidden
    }
});