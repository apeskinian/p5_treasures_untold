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