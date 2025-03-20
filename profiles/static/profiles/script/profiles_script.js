/* jshint esversion: 11 */
/* globals bootstrap */
// Showing modal if there is an order history request.
window.onload = () => {
    const orderHistoryModalElement = document.getElementById('order-history-modal');
    if (orderHistoryModalElement) {
        const orderHistoryModal = new bootstrap.Modal(orderHistoryModalElement);
        orderHistoryModal.show();
    }
};

//Adding spinner to submit button on submit
const submitButton = document.getElementById('profile-submit-button');

submitButton.addEventListener('click', function(event) {
    submitButton.querySelector('#btn-text').classList.add('d-none');
    submitButton.querySelector('.spinner').classList.remove('d-none');
    submitButton.classList.add('disabled');
})